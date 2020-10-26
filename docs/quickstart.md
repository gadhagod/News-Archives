### Quckstart
It's incredibly simple to start using this service. <br>Make the following request:

    GET http://newsarchive.herokuapp.com/
On your command line, that would look like:

    curl http://newsarchive.herokuapp.com/

This would retrieve you _all_ data stored since 2020-10-26. The response should be similar to this (articles were randomly picked from 2020-10-23):

    {data:
        [
            {
                "date": "2020-10-23",
                "articles": [
                    {
                        "title": "China warns UK not to offer citizenship to Hong Kong residents",
                        "description": "The UK plans to offer a path to citizenship to many in Hong Kong after Beijing's new security law.",
                        "link": "https://www.bbc.com/news/world-asia-china-54655285"
                    },
                    {
                        "title": "Bihar elections: Huge crowds gather at rallies, raising coronavirus fears",
                        "description": "Experts warn flouting of safety rules at India rallies could have devastating consequences.",
                        "link": "https://www.bbc.co.uk/news/world-asia-india-54657433"
                    },
                    {more articles...}
                ]
            },
            {
                "date": "2020-10-24",
                "articles": [
                    {more articles...}
                ]
            },
            {more days...}
        ]
    }

In the JSON above, all data is under the key `data`. Under `data`, there's a list which contains JSON objects, each signifying a day. Under each day, there's a date and a list of articles. Each item under `articles` is a JSON object with the article's `title`, `description`, and `link`.