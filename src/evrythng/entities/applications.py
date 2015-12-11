from evrythng import utils
from . import validate_field_specs


field_specs = {
    'datatypes': {
        'name': 'str',
        'description': 'str',
        'project': 'ref',
        'defaultUrl': 'str',
        'socialNetworks': 'list_of_social_networks',
        'tags': 'list_of_str',
        'customFields': 'dict_of_str',
        'appApiKey': 'str',
    },
    'required': ('name', 'socialNetworks'),
    'readonly': ('id', 'createdAt', 'updatedAt', 'project', 'appApiKey'),
    'writable': ('description', 'defaultUrl', 'tags', 'customFields'),
}


def create_application(project_id, name=None, description=None,
                       defaultUrl=None, socialNetworks=None, tags=None,
                       customFields=None, appApiKey=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    validate_field_specs(kwargs, field_specs)
    url = '/projects/{}/applications'.format(project_id)
    return utils.request('POST', url, data=kwargs, api_key=api_key)


def update_application(project_id, application_id, name=None, description=None,
                       defaultUrl=None, socialNetworks=None, tags=None,
                       customFields=None, appApiKey=None, api_key=None):
    kwargs = locals()
    api_key = kwargs.pop('api_key', None)
    project_id = kwargs.pop('project_id')
    application_id = kwargs.pop('application_id')
    validate_field_specs(kwargs, field_specs)
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('PUT', url, data=kwargs, api_key=api_key, accept=True)


def list_applications(project_id, api_key=None):
    url = '/projects/{}/applications'.format(project_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def read_application(project_id, application_id, api_key=None):
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('GET', url, api_key=api_key, accept=True)


def delete_application(project_id, application_id, api_key=None):
    url = '/projects/{}/applications/{}'.format(project_id, application_id)
    return utils.request('DELETE', url, api_key=api_key, accept=True)
