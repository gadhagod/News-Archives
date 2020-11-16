### Python

##### Installation

    pip3 install newsarchives

##### Methods
- `time().day('day-as-string')`: Get articles from a day
- `time().month('month-as-string')`: Get articles from a month
- `time().year('year-as-string')`: Get articles from a year
- `keyword('keyword-as-string')`: Get articles with a keyword

##### Example
    # Get articles of a given day

    import newsarchives
    
    target_day = input('What day would you like to search for? ')
    for article in newsarchives.time().day(target_day):
        print(article['title'])