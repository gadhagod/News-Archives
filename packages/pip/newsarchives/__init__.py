'''
newsarchives
The official python client library for the News Archives API.
By Aarav Borthakur

Docs: https://gadhagod.github.io/News-Archives
Github: https://github.com/gadhagod/News-Archives
'''

import requests

def make_request(url, timeout=False):
    if timeout:
        return(requests.get(url, timeout=timeout).json())
    else:
        return(requests.get(url).json())

class time():  
    def day(self, day, timeout=False):
        url = 'http://newsarchives.herokuapp.com/day/' + day
        return(make_request(url, timeout))

    def month(self, month, timeout=False):
        url = 'http://newsarchives.herokuapp.com/month/' + month
        return(make_request(url, timeout))

    def year(self, year, timeout=False):
        url = 'http://newsarchives.herokuapp.com/year/' + year
        return(make_request(url, timeout))

def keyword(keyword, timeout=False):
    url = 'http://newsarchives.herokuapp.com/keyword/' + keyword
    return(make_request(url, timeout))