'
newsarchives
The official ruby client library for the News Archives API.
By Aarav Borthakur

Docs: https://gadhagod.github.io/News-Archives
Github: https://github.com/gadhagod/News-Archives
'

require 'net/http'
require 'json'

def req(endpoint)
    response = Net::HTTP.get_response(URI.parse('https://newsarchives.herokuapp.com/' + endpoint))
    return JSON.parse(response.body)
end

class Time
    def day(day)
        return req('/day/' + day)
    end
    def month(month)
        return req('/month/' + month)
    end
    def year(year)
        return req('/year/' + year)
    end
end

def keyword(keyword)
    return req('/keyword/' + keyword)
end