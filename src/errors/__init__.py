def err_500():
    return({'message': 'internal server error', 'status': 500})

def err_400():
    return({'message': 'URL not found', 'status': 404})