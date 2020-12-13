def percent(numbers):
    total = 0
    for number in numbers:
        total = total + number
    percents = []
    for number in numbers:
        percents.append('{}%'.format((round((number / total) * 100))))
    return(percents)

def refine(input):
    input_list = list(input)
    for item in input_list:
        item['date'] = item.pop('_id')
        item.pop('_event_time', None)
    return(input_list)