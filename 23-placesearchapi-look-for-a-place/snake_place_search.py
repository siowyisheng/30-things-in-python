import requests
from pprint import pprint
from key import key

parameters_dict = {
    'key': key,
    'input': 'snakes singapore',
    'inputtype': 'textquery',
    'fields': 'name,place_id',
}

parameters = '&'.join(
    ['{}={}'.format(key, value) for key, value in parameters_dict.items()])

url = 'https://maps.googleapis.com/maps/api/place/findplacefromtext/json?{}'.format(
    parameters)
r = requests.get(url)
pprint(r.json())
