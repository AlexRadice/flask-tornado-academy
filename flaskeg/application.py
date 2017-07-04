from flaskeg.datastore import get_all, get_user
from flaskeg.developerdetailscontroller import DeveloperDetailsController
from flaskeg.authentication import FlaskLoginUser, load_identity, save_identity
from flaskeg.login import LoginController
from flask import Flask, render_template, session
from flask_login import LoginManager, current_user
from flask_principal import Principal

app = Flask('flaskeg')
app.secret_key = "really_secret_key"


# Authentication
login_manager = LoginManager()
login_manager.init_app(app)

@login_manager.user_loader
def load_user(user_id):
    "Load user"
    user = get_user(user_id)
    return FlaskLoginUser(user)


# Authorisation
principals = Principal(app)
principals.identity_loader(load_identity)
principals.identity_saver(save_identity)


# Controllers
@app.route('/')
def index():
    "Home page"
    return render_template('index.html', developers=get_all())

app.add_url_rule('/developer', view_func=DeveloperDetailsController.as_view('developer'))
app.add_url_rule('/login', view_func=LoginController.as_view('login'))



# Jinja customisation
def get_version():
    "Get application version"
    return '0.9.9.9.9.9.9.9'

def polite(name):
    "Return an extra polite name"
    return u"Sir {}".format(name)

def is_cellA(cell):
    "Return True if this is cell A"
    return cell == 'A'

app.jinja_env.globals['get_version'] = get_version
app.jinja_env.filters['polite'] = polite
app.jinja_env.tests['is_cellA'] = is_cellA


if __name__ == '__main__':
    app.run(port=11000, debug=True) 
