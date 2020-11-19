from bbc_feeds import *
from rockset import Client, Q, F
from os import environ
from datetime import date, datetime
from time import sleep

def update_collection(date, content):
    collection_name = 'NewsArchives'
    rs = Client(api_key = environ.get('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')
    collection = rs.Collection.retrieve(collection_name)

    docs = {
        '_id': date,
        'articles': content
    }
    print(collection.add_docs([docs]))

def add_docs():
    ls = []
    for i in news().world():
        ls.append(
            {
                'title': i['title'],
                'link': i['links'][0]['href'],
                'description': i['summary']
            }
        )
    update_collection(date.today(), ls)

while True:
    if datetime.now().strftime('%H') == '10':
        add_docs()
        sleep(3600*2)
    else:
        print(datetime.now().strftime('%H'))
        sleep(60)
