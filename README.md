# Welcome to News Archives REST API
The #1 Historic News API.

![](https://heroku-status-badges.herokuapp.com/newsarchives)
![](https://img.shields.io/github/last-commit/gadhagod/News-Archives?color=lightblue&label=last%20updated)
![](https://img.shields.io/pypi/v/newsarchives?color=blue)
![](https://img.shields.io/gem/v/newsarchives?color=darkred)

## Concept
Starting October 29, 2020, trending news from BBC has been logged for the public, and will continue for years. So, in say, a decade, you will be able to see what was on the news today. \
Why is this useful? 
- Since just October 29, much has happened. Imagine all the historic events that will happen in the next few years.
- You can get past daily "coverage" of happenings with huge impacts, like the presidential race.
- Maybe you want to relive the events and people reactions to the road to the coronavirus vaccine.
- Perhaps you just want to see what was on the news on your 10th birthday?


**News Archives** has made this all possible! You can get news from a day, month, year, or with a keyword in milliseconds.


## Requests
**Base URL**:
[https://newsarchives.herokuapp.com/api/v2](https://newsarchives.herokuapp.com/api/v2)

**Endpoints**: 

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

    curl https://newsarchives.herokuapp.com/api/v2/day/2020-11-02

Get all data from month 2020-11:

    curl https://newsarchives.herokuapp.com/api/v2/month/2020-11

Get all data with keyword "Trump" from 2020:

    curl https://newsarchives.herokuapp.com/api/v2/keyword/trump?year=2020

Get five most recent mentions of keyword "China":

    curl https://newsarchives.herokuapp.com/api/v2/keyword/china?limit=5

## Client Libraries
Client libraries are available for python and ruby. More are coming soon.

## Demo App

View a demo app at this [site](https://newsarchives.herokuapp.com/demo). It's source code is in this [GitHub Repository](https://github.com/gadhagod/News-Archives).

## Progress Updates

Check out this [project](https://github.com/gadhagod/News-Archives/projects/1) for progress updates.

## Source

The code is licensed under the [MIT License](https://github.com/gadhagod/News-Archives/blob/master/LICENSE). It's open source, so you can find the source code [here](https://github.com/gadhagod/News-Archives). Pull requests and suggestions are encouraged.

## Architecture
[Here](https://gadhagod.medium.com/how-i-built-the-news-archives-api-dfcb3b12d4f6) is an article about how this project was built.
