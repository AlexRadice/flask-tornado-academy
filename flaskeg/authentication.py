from flask_login import UserMixin, current_user
from flask_principal import Permission, RoleNeed

_identities = {}

EDIT_USER_ROLE = RoleNeed('EditUser')
EDIT_USER_PERMISSION = Permission("Edit User", EDIT_USER_ROLE)


def load_identity():
    "Load identity"
    if current_user.is_authenticated:
        return _identities.get(current_user.get_id())
    else:
        return None


def save_identity(identity):
    "Save identity"
    _identities[identity.id] = identity



class FlaskLoginUser(UserMixin):
    "Class representing a Flask user"

    def __init__(self, user):
        self._user_id = user.get('mail')
        self._name = user.get('name')


    @property
    def is_authenticated(self):
        "Is user authenticated"
        return True


    @property
    def is_active(self):
        "Is user active"
        return True


    @property
    def is_anonymous(self):
        "Is user anonymous"
        return False


    def get_id(self):
        "Get user id"
        return unicode(self._user_id)


    def get_name(self):
        "Get user name"
        return self._name


