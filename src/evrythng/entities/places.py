from evrythng import utils
from . import validate_field_specs


field_specs = {
    'datatypes': {
        'position': 'geojson',
        'address': 'address',
        'description': 'str',
        'icon': 'str',
        'tags': 'list_of_str',
        'customFields': 'dict_of_str',
    },
    'required': ('name',),
    'readonly': ('id', 'createdAt', 'updatedAt'),
    'writable': ('position', 'address', 'description', 'icon', 'tags',
                 'customFields'),
}


def create_place(name, position=None, address=None, description=None,
                 icon=None, tags=None, customFields=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    validate_field_specs(kwargs, field_specs)
    return utils.request('POST', '/places', data=kwargs)


def read_place(place_id, api_key=None):
    url = '/places/{}'.format(place_id)
    return utils.request('GET', url, api_key=api_key)


def update_place(place_id, name=None, position=None, address=None, description=None,
                 icon=None, tags=None, customFields=None):
    kwargs = locals()
    place_id = kwargs.pop('place_id')
    api_key = kwargs.pop('api_key', None)
    validate_field_specs(kwargs, field_specs)
    url = '/places/{}'.format(place_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key)


def delete_place(place_id, api_key=None):
    url = '/places/{}'.format(place_id)
    return utils.request('DELETE', url, api_key=api_key)


def list_places(api_key=None):
    return utils.request('GET', '/places', api_key=api_key)
