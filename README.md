# Welcome to News Archives REST API

![](https://heroku-status-badges.herokuapp.com/newsarchives)

**The #1 Historic News API.** In five years, you will be able to see today's news. You can see news from any day, month, year, or containing a keyword. With quick responses and with simply organized JSON responses, even beginners can get started. No authorization is required for this API.

## Requests
**URL**:
[https://newsarchives.herokuapp.com/api/v1](https://newsarchives.herokuapp.com/api/v1)

**Arguments**: 

* `day`: Get data on a day
* `month`: Get data on a month
* `year`: Get data on a year
* `keyword`: Get data with a keyword. You can specify a time frame using arguements day, month, and year. Optional arguments for keyword:
    * `day`: Get articles with a keyword on a specific day.
    * `month`: Get articles with a keyword on a specific month.
    * `year`: Get articles with a keyword in a specific year.
    * `limit`: Limit the number of responses, returns most recent data.

## Examples
Get all data from 2020-11-02:

    curl https://newsarchives.herokuapp.com/api/v1?day=2020-11-02

Get all data from 2020-11:

    curl https://newsarchives.herokuapp.com/api/v1?month=2020-11

Get all data with keyword "Trump" from 2020:

    curl https://newsarchives.herokuapp.com/api/v1?keyword=trump&year=2020

Get five most recent mentions of keyword "China":

    curl https://newsarchives.herokuapp.com/api/v1?keyword=china&limit=5

## Demo App

View a demo app at this [site](https://newsarchives.herokuapp.com/demo). It's source code is in this [GitHub Repository](https://github.com/gadhagod/News-Archives).

## Progress Updates

Check out this [project](https://github.com/gadhagod/News-Archives/projects/1) to see progress updates.

## Source

The code is licensed under the [MIT License](https://github.com/gadhagod/News-Archives/blob/master/LICENSE). It's open source, so you can find the source code [here](https://github.com/gadhagod/News-Archives). Pull requests and suggestions are encouraged.
