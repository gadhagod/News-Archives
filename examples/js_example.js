// Get all data from 2020-10-29
const request = require('request')

request('http://newsarchives.herokuapp.com/api/v1-alpha?day=2020-10-29', function (error, response, body) {
    console.log((body))
})