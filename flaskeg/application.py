from flaskeg.datastore import get_all, get_user
from flaskeg.developerdetailscontroller import DeveloperDetailsController
from flaskeg.authentication import FlaskLoginUser, load_identity, save_identity
from flaskeg.login import LoginController
from flask import Flask, render_template, session
from flask_login import LoginManager, current_user
from flask_principal import Principal

app = Flask('flaskeg')
app.secret_key = "really_secret_key"
login_manager = LoginManager()
login_manager.init_app(app)
principals = Principal(app)

@login_manager.user_loader
def load_user(user_id):
    "Load user"
    user = get_user(user_id)
    return FlaskLoginUser(user)

principals.identity_loader(load_identity)
principals.identity_saver(save_identity)

@app.route('/')
def index():
    "Home page"
    return render_template('index.html', developers=get_all())

app.add_url_rule('/developer', view_func=DeveloperDetailsController.as_view('developer'))
app.add_url_rule('/login', view_func=LoginController.as_view('login'))

if __name__ == '__main__':
    app.run(port=11000, debug=True) 
