from flask import render_template
import newsarchives as archiveslib

def index():
    return(render_template('demo.jinja'))

def day_search(day):
    return(render_template('demo_search.jinja', news=archiveslib.day(day)['data'][0]['articles']))

def keyword_search(target):
    return(render_template('demo_search.jinja', news=archiveslib.keyword(target, limit=20)['data'], keyword=target))
    