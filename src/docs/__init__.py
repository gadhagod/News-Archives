import os
from flask import render_template
from requests import get

def percent(numbers):
    total = 0
    for number in numbers:
        total = total + number
    percents = []
    for number in numbers:
        percents.append('{}%'.format((round((number / total) * 100))))
    return(percents)

def home():
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