from flask import Flask, request
from rockset import Client, ParamDict, Q, F
import os

# Retrive collection
rs = Client(api_key=os.environ.get('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')
newsarchives = rs.Collection.retrieve('NewsArchives')

# Retrive query lambdas
keyword_search = rs.QueryLambda.retrieve('NewsKeywordSearch', version='42add4ea34c9b93d', workspace='commons')
time_keyword_search = rs.QueryLambda.retrieve('NewsTimeKeywordSearch', version='1b860b6f602f8e09', workspace='commons')

app = Flask(__name__)

def refine(input):
    input_list = list(input)
    for item in input_list:
        item['date'] = item.pop('_id')
        try:
            del item['_event_time']
        except:
            pass
    return(input_list)

@app.route('/api/v1-alpha', methods=['GET'])
def main():
    args = request.args.to_dict() # get url arguments
    try:
        limit_count = int(args['limit']) # if a limit is specified, set the limit
    except:
        limit_count = 1000000 # else, limit is million
    try:
        order = args['order'] # if an order is given, get it
    except:
        order = 'recent' # else, set the order to 'recent'

    args['limit'] = limit_count # set limit to variable
    num_of_time_recieved = 0 # number of time args set to 0
    # set args to False if not specified
    try:
        keyword = args['keyword']
    except:
        keyword = False
    try:
        day = args['day']
        num_of_time_recieved = num_of_time_recieved + 1
    except:
        day = False
    try:
        month = args['month']
        num_of_time_recieved = num_of_time_recieved + 1
    except:
        month = False
    try:
        year = args['year']
        num_of_time_recieved = num_of_time_recieved + 1
    except:
        year = False

    if num_of_time_recieved > 1:
        # if more than one time argument recieved, return error
        return({'message': 'more than one time argument recieved', 'parameters': args, 'status': 400})

    if not keyword and num_of_time_recieved == 1:
        # one time arg is given
        if day:
            # day is the given time arg
            res = list(
                rs.sql(Q('NewsArchives').where(F['_id'] == day).select(F['articles'])))
            print(res)
            return({'date': day, 'data': res, 'parameters': args, 'status': 200})
        if month:
            # month is the given time arg
            res = list(rs.sql(Q('NewsArchives').where(F['_id'].like(month + '%'))))
            return({'data': refine(res), 'parameters': args, 'status': 200})
        if year:
            # year is the given time arg
            res = list(rs.sql(Q('NewsArchives').where(F['_id'].like(year + '%'))))
            return({'data': refine(res), 'parameters': args, 'status': 200})

    if keyword and num_of_time_recieved == 0:
        # only keyword is given
        parameters = ParamDict()
        parameters['keyword'] = keyword
        parameters['limit'] = limit_count
        res = keyword_search.execute(parameters=parameters).to_dict()['results']
        return({'data': refine(res), 'parameters': args, 'status': 200})

    if keyword and num_of_time_recieved == 1:
        # if a keyword and a time arg is given
        parameters = ParamDict()
        parameters['keyword'] = keyword
        if day:
            parameters['time'] = day
        if month:
            parameters['time'] = month
        if year:
            parameters['time'] = year
        parameters['limit_count'] = limit_count
        res = time_keyword_search.execute(parameters=parameters).to_dict()['results']
        return({'data': refine(res), 'parameters': args, 'status': 200})
    
    return({'message': 'ready', 'parameters': args, 'status': 200})

@app.errorhandler(500)
def server_error(err):
    return({'message': 'internal server error', 'status': 500})

@app.errorhandler(404)
def not_found(err):
    return({'message': 'URL not found', 'status': 404})