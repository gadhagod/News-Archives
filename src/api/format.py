def refine(input):
    input_list = list(input)
    for item in input_list:
        item['date'] = item.pop('_id')
        item.pop('_event_time', None)
    return(input_list)