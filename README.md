# Welcome to News Archives REST API

The #1 historic news API.

## Server

#### URL format
**Base URL**:

    https://newsarchives.herokuapp.com

**Endpoints**:

- `/api/v1-alpha`

## Requests

**Arguments**: <br>
1. `day`: Get data on a day <br>
2. `month`: Get data on a month<br>
3. `year`: Get data on a year<br>
4. `keyword`: Get data with a keyword. You can specify a time frame using arguements day, month, and year. Optional arguments for keyword:<br>
    - `day`: Get articles with a keyword on a specific day.<br>
    - `month`: Get articles with a keyword on a specific month.<br>
    - `year`: Get articles with a keyword in a specific year.<br>
    - `limit`: Limit the number of responses, returns most recent data.

## Examples
Get all data from 2020-11-02:

    curl https://newsarchives.herokuapp.com/api/v1-alpha?day=2020-11-02

Get all data from 2020-11:

    curl https://newsarchives.herokuapp.com/api/v1-alpha?month=2020-11

Get all data with keyword "Trump" from 2020:

    curl https://newsarchives.herokuapp.com/api/v1-alpha?keyword=trump&year=2020

Get five most recent mentions of keyword "China":

    curl https://newsarchives.herokuapp.com/api/v1-alpha?keyword=china&limit=5

## Progress Updates
Subscribe to this [issue thread](https://github.com/gadhagod/News-Archives/issues/2) to get progress updates.