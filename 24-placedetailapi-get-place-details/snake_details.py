import requests
from pprint import pprint
from key import key

parameters_dict = {
    'key': key,
    'placeid': 'ChIJyWpkZzAY2jERo5VX6ziM2x8',
}

parameters = '&'.join(
    ['{}={}'.format(key, value) for key, value in parameters_dict.items()])

url = 'https://maps.googleapis.com/maps/api/place/details/json?{}'.format(
    parameters)
r = requests.get(url)
pprint(r.json())