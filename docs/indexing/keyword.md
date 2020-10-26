### Indexing by Keyword
You can get all articles that have a certain keyword in their description or title by making the following request:

    GET http://newsarchives.herokuapp.com/keyword/{keyword}

##### Sample Request

    curl http://newsarchives.herokuapp.com/keyword/trump

You should get all articles with keyword "Trump".