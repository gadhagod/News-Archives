# Get five most recent mentions of "india"
require 'net/http'
require 'json'

response = Net::HTTP.get_response(URI.parse('https://newsarchives.herokuapp.com/api/v1-alpha?keyword=india&limit=5'))
puts JSON.parse(response.body)