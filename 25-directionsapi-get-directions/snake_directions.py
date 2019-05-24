import requests
from pprint import pprint
from key import key

parameters_dict = {
    'key': key,
    'origin': 'Raffles+Institution',
    'destination': 'Asia+Snakes+Pte+Ltd',
    'mode': 'transit',
}
parameters = '&'.join(
    ['{}={}'.format(key, value) for key, value in parameters_dict.items()])

url = 'https://maps.googleapis.com/maps/api/directions/json?{}'.format(
    parameters)
r = requests.get(url)
pprint(r.json())
print('{} public transit routes found.'.format(len(r.json()['routes'])))