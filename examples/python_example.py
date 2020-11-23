# Get all mentions of "russia" in 2020-11.
from requests import get

print(get('http://newsarchives.herokuapp.com/api/v1-alpha?month=2020-11&keyword=russia').json())