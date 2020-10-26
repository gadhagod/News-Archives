### Indexing by Keyword
You can get all articles that have a certain keyword in their description or title by making the following request:

    GET http://newsarchives.herokuapp.com/keyword/{keyword}

##### Sample Request

    curl http://newsarchives.herokuapp.com/keword/trump

You should get all articles with keyword "Trump".

!> Indexing by keyword returns a different format of data. The date will be inside the article's information.