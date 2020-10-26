from BBCHeadlines import articles
from rockset import Client, Q, F
from os import environ
from datetime import date, datetime
from time import sleep

def upd(date, content):
    collection_name = 'NewsArchives'
    rs = Client(api_key = environ.get('ROCKSET_SECRET'), api_server='api.rs2.usw2.rockset.com')
    collection = rs.Collection.retrieve(collection_name)

    docs = {
        '_id': date,
        'articles': content
        }
    print(collection.add_docs([docs]))

def main():
    ls = []
    titles = articles.title()
    links = articles.link()
    descriptions = articles.description()
    for i in range(len(articles.title())):
        ls.append(
            {
                'title': titles[i],
                'link': links[i],
                'description': descriptions[i]
            }
        )
    upd(date.today(), ls)

while True:
    if datetime.now().strftime('%H') == '10':
        main()
        sleep(3600*2)
    else:
        print(datetime.now().strftime('%H'))
        sleep(60)
