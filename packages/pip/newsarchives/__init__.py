import requests

class Error(Exception):
    pass

class Non200CodeError(Error):
    pass

def day(target_day):
    res = requests.get('http://newsarchives.herokuapp.com/api/v1-alpha', params={'day': target_day}).json()
    if res['status'] != 200:
        raise Non200CodeError('The server responded with a non-200 code: ' + res['message'])
    return(res)

def month(target_month):
    res = requests.get('http://newsarchives.herokuapp.com/api/v1-alpha', params={'month': target_month}).json()
    if res['status'] != 200:
        raise Non200CodeError('The server responded with a non-200 code: ' + res['message'])
    return(res)

def year(target_year):
    res = requests.get('http://newsarchives.herokuapp.com/api/v1-alpha', params={'year': target_year}).json()
    if res['status'] != 200:
        raise Non200CodeError('The server responded with a non-200 code: ' + res['message'])
    return(res)

def keyword(target_keyword, day=False, month=False, year=False, limit=False):
    num_of_time_args = 0
    params = {}
    time = False

    if day:
        num_of_time_args = num_of_time_args + 1
        time = 'day'
        params[time] = day
    if month:
        num_of_time_args = num_of_time_args + 1
        time = 'month'
        params[time] = month
    if year:
        num_of_time_args = num_of_time_args + 1
        time = 'year'
        params[time] = year

    if limit:
        params['limit'] = limit

    params['keyword'] = target_keyword
    res = requests.get('http://newsarchives.herokuapp.com/api/v1-alpha', params=params).json()
    if res['status'] != 200:
        raise Non200CodeError('The server responded with a non-200 code: ' + res['message'])
    return(res) 