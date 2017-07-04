from flask import Flask, render_template
from flaskeg.datastore import get_all
from flaskeg.developerdetailscontroller import DeveloperDetailsController

if __name__ == '__main__':
    app = Flask('flaskeg')

    @app.route('/')
    def index():
        "Home page"
        return render_template('index.html', developers=get_all())

    app.add_url_rule('/developer', view_func=DeveloperDetailsController.as_view('developer'))

    app.run(port=11000, debug=True) 
