from flask import Flask, request, jsonify
from rockset import Client, ParamDict, Q, F
import os
from datetime import date, datetime

collection_name = 'NewsArchives'
rs = Client(api_key=os.environ.get('ROCKSET_SECRET'), api_server="api.rs2.usw2.rockset.com")
collection = rs.Collection.retrieve(collection_name)
app = Flask(__name__)

def refine(j, meth=''):
    ls = list(j)
    for i in ls:
        i['date'] = i.pop('_id')
        del i['_event_time']

    if meth == 'all':
        return({'data': ls})

    if meth == 'single':
        return({'data': ls[0]})

    return(i)

@app.route('/', methods=['GET'])
def funcall():
    return(refine(rs.sql(Q(collection_name)), 'all'))

@app.route('/day/<day>', methods=['GET'])
def funcdate(day):
    return(refine(list(rs.sql(Q(collection_name).where(F['_id'] == day).select(F['*']))), 'single'))

@app.route('/month/<month>', methods=['GET'])
def funcmonth(month):
    res = list(rs.sql(Q(collection_name).where(F['_id'].like(month + '%'))))
    ls = []
    for i in res:
        target = i['_id']
        target_year = target[:target.index('-')]
        target_month_day = target[target.index('-'):].replace('-', '', 1)
        target_month = target_month_day[:target_month_day.index('-')]
        print('In: '+  month + 'i: ' + target_year + '-' + target_month)
        if month == target_year + '-' + target_month:
            ls.append(i)
    return(
        refine(ls, 'all')
    )

@app.route('/year/<year>')
def funcyear(year):
    res = list(rs.sql(Q(collection_name).where(F['_id'].like(year + '%'))))
    ls = []
    for i in res:
        if year == i['_id'][:i['_id'].index('-')]:
            ls.append({
                'date': i['_id'],
                'articles': i['articles'],
            })
    num = 0
    for i in ls:
        for x in i['articles']:
            num = num + 1
    return({
        'data': ls
    })

@app.route('/keyword/<keyword>', methods=['GET'])
def funckeyword(keyword):
    qlambda = rs.QueryLambda.retrieve(
        'NewsKeywordSearch',
        version='df3d671743c064d2',
        workspace='commons'
    )
    params = ParamDict()
    params['keyword'] = keyword
    results = qlambda.execute(parameters=params).to_dict()['results']
    for i in results:
        i['date'] = i.pop('_id')
    return({
        'data': results
    })