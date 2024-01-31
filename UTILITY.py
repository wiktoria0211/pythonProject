from geopy.geocoders import Nominatim
from shapely import wkb

def convert_point(wkb_point):
    point = wkb.loads(str(wkb_point), hex=True)
    return (point.y, point.x)

def get_coords(address):
    geolocator = Nominatim(user_agent="my_geocoder")
    location = geolocator.geocode(address)

    latitude, longitude = location.latitude, location.longitude
    return latitude, longitude