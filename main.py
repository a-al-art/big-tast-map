import sys
from io import BytesIO  # Этот класс поможет нам сделать картинку из потока байт

import requests
from PIL import Image
from geocoder import get_ll_span
from mapapi_PG import show_map

coordinates = '151.21531815767764,-33.85673985210281'
z = 17
show_map(coordinates, map_type='sat', add_params={'z': z})
