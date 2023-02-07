import requests


def get_map(ll=None, map_type="map", add_params=None):
    api_server = 'http://static-maps.yandex.ru/1.x/'
    params = {'l': map_type}
    if ll is not None:
        params['ll'] = ll

    if add_params is not None:
        params.update(add_params)

    return requests.get(api_server, params)
