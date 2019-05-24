from geopy.geocoders import Nominatim
from geopy.distance import geodesic
from pprint import pprint

geolocator = Nominatim(user_agent="snakes-distance-geopy")
school = geolocator.geocode("raffles institution singapore")

print('Snakey school is located at {}'.format(school.address))
print('Snakey school\'s coordinates are ({}, {}) '.format(
    school.latitude, school.longitude))

home = geolocator.geocode("58 college green singapore")
print('Home is located at {}'.format(home.address))

home_coordinates = home.latitude, home.longitude
school_coordinates = school.latitude, school.longitude
distance = geodesic(home_coordinates, school_coordinates).km
print('The distance from home to school is {:.2f} km'.format(distance))