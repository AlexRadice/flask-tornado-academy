from flask_login import UserMixin

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


