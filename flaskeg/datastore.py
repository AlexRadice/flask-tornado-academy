"Data store for developers"

_developers = {'Alex Radice': {
    'name': 'Alex Radice',
    'cell': 'A',
    'favouritefruit': 'grapefruit'
}}

_users = {'billy.bob@inter.net': {
        'name': 'Billy Bob',
        'mail': 'billy.bob@inter.net'
    }}


def get_all():
    "Get all developers"
    return _developers.values()


def get_developer(name):
    "Get a named developer"
    return _developers.get(name)


def save_developer(developer):
    "Save the developer"
    _developers[developer['name']] = developer


def new_developer():
    "Get a blank object for a new developer"
    return {'name': '',
        'cell': '',
        'favouritefruit': ''}


def get_user(mail):
    "Get user by email address"
    return _users.get(mail)

