import os
from requests import get
from flask import Flask, request, render_template
from flaskext.markdown import Markdown
from rockset import Client, ParamDict, Q, F
import demo

# Retrive collection
rs = Client(api_key=os.environ.get('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')
newsarchives = rs.Collection.retrieve('NewsArchives')

# Retrive query lambdas
keyword_search = rs.QueryLambda.retrieve('NewsKeywordSearch', version='42add4ea34c9b93d', workspace='commons')
time_keyword_search = rs.QueryLambda.retrieve('NewsTimeKeywordSearch', version='1b860b6f602f8e09', workspace='commons')

app = Flask(__name__)
Markdown(app)

def percent(numbers):
    total = 0
    for number in numbers:
        total = total + number
    percents = []
    for number in numbers:
        percents.append('{}%'.format((round((number / total) * 100))))
    return(percents)

def refine(input):
    input_list = list(input)
    for item in input_list:
        item['date'] = item.pop('_id')
    return(input_list)

@app.route('/api/v1-alpha', methods=['GET'])
@app.route('/api/v1', methods=['GET'])
def main():
    args = request.args.to_dict() # get url arguments
    try:
        limit_count = int(args['limit']) # if a limit is specified, set the limit
    except:
        limit_count = 1000000 # else, limit is million

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

@app.route('/', methods=['GET'])
def docs():
    languages = get('https://api.github.com/repos/gadhagod/News-Archives/languages', headers={'Authorization': 'token: {}'.format(os.getenv('GITHUB_TOKEN'))}).json()
    lang_list = []
    for langauge in languages:
        lang_list.append(languages[langauge])
    percents = percent(lang_list)
    loop = 0
    for langauge in languages:
        languages[langauge] = percents[loop]
        loop = loop + 1
    return(render_template(
            'index.jinja', 
            README=get('https://raw.githubusercontent.com/gadhagod/News-Archives/master/README.md').text.replace('&amp;', '&'),
           languages=languages
        )
    )

@app.route('/demo', methods=['GET'])
def homepage():
    return(demo.index())

@app.route('/demo/day/<target>', methods=['GET'])
def server_day_search(target):
    return(demo.day_search(target))

@app.route('/demo/keyword/<target>', methods=['GET'])
def server_keyword_search(target):
    return(demo.keyword_search(target))

@app.errorhandler(500)
def server_error(err):
    return({'message': 'internal server error', 'status': 500})

@app.errorhandler(404)
def not_found(err):
    return({'message': 'URL not found', 'status': 404})