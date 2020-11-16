### Ruby

##### Installation

    gem install newsarchives
require 'newsarchives'

time = Time.new
puts time.year('2020')
puts keyword('trump')

puts "Enter your name: "
name = gets.chomp
puts "Hello #{name}, how are you"

##### Methods
- `time().day('day-as-string')`: Get articles from a day
- `time().month('month-as-string')`: Get articles from a month
- `time().year('year-as-string')`: Get articles from a year
- `keyword('keyword-as-string')`: Get articles with a keyword

##### Example

    # Get articles with a keyword

    require 'newsarchives'

    puts "What keyword would you like to search for? "
    target_keyword = gets

    puts keyword(target_keyword)    