from flask import render_template
import newsarchives as archiveslib

def index():
    return(render_template('index.html'))

def day_search(day):
    return(render_template('search.html', news=archiveslib.day(day)['data'][0]['articles']))

def keyword_search(target):
    return(render_template('search.html', news=archiveslib.keyword(target, limit=20)['data']))
    