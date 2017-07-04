from flask import render_template, redirect, request
from flask.views import MethodView
from flaskeg.datastore import get_user
from flaskeg.authentication import FlaskLoginUser
from flask_login import login_user

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
        return redirect('/')


