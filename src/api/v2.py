import os
from requests import get
from flaskext.markdown import Markdown
from rockset import Client, ParamDict, Q, F
from format import refine

rs = Client(api_key=os.getenv('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')

# Retrive query lambdas
keyword_search = rs.QueryLambda.retrieve('NewsKeywordSearch', version='42add4ea34c9b93d', workspace='commons')
time_keyword_search = rs.QueryLambda.retrieve('NewsTimeKeywordSearch', version='fadd403949d105e7', workspace='commons')

def base():
    return({'message': 'ready', 'status': 200})

def day(target):
    return(
        {
            'date': target, 'data': list(
                rs.sql(
                    Q('NewsArchives').where(F['_id']==target).select(F['articles'])
                )
            ), 'status': 200
        }
    )

def month(target):
    return(
        {
            'data': refine(
                rs.sql(
                    Q('NewsArchives').where(F['_id'].like(target + '%'))
                )
            ), 'status': 200
        }
    )

def year(target):
    return(
        {
            'data': refine(
                rs.sql(
                    Q('NewsArchives').where(F['_id'].like(target + '%'))
                )
            ), 'status': 200
        }
    )

def keyword(target, args):
    q_params = ParamDict()
    q_params['keyword'] = target
    keys = list(args.keys())
    num_time_args = 0
    if 'limit' in keys:
        q_params['limit'] = int(args['limit'])
    else:
        q_params['limit'] = 1000000
    if 'day' in keys:
        num_time_args = num_time_args + 1
        q_params['time'] = args['day']
    if 'month' in keys:
        num_time_args = num_time_args + 1
        q_params['time'] = args['month']
    if 'year' in keys:
        num_time_args = num_time_args + 1
        q_params['time'] = args['year']
    if num_time_args > 1:
        return({'message': 'Too many time arguments', 'status': 402})
    if num_time_args == 0:
        return(
            {
                'data': refine(
                    keyword_search.execute(parameters=q_params).to_dict()['results']
                ), 'status': 200
            }
        )

    else:
        return(
            {
                'data': refine(
                    time_keyword_search.execute(parameters=q_params).to_dict()['results']
                ), 'status': 200
            }
        )