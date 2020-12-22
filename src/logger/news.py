from bbc_feeds import news

ls = []
for article in news().world():
    ls.append({
        'title': article['title'],
        'description': article['summary'],
        'link': article['links'][0]['href']
    })
print(str(ls).replace('\'', '"'))