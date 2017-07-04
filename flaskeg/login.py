from flaskeg.datastore import get_user
from flaskeg.authentication import FlaskLoginUser, EDIT_USER_ROLE
from flask import render_template, redirect, request, current_app
from flask.views import MethodView
from flask_login import login_user
from flask_principal import Identity, identity_changed

class LoginController(MethodView):
    "Login controller"

    def get(self):
        "Return login screen"
        return render_template('login.html')


    def post(self):
        "Handle login"
        if request.form.get('Cancel'):
            return redirect('/')
        mail = request.form.get('mail')
        user = get_user(mail)
        flask_user = FlaskLoginUser(user)
        login_user(flask_user)
        identity = Identity(flask_user.get_id())
        identity.provides.add(EDIT_USER_ROLE)
        identity_changed.send(current_app._get_current_object(), identity=identity)
        return redirect('/')


