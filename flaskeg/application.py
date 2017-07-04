from flask import Flask

if __name__ == '__main__':
    app = Flask('flaskeg')

    @app.route('/')
    def index():
        "Home page"
        return '<html><body><h1>This is the home page!</h1></body></html>'

    app.run(port=11000, debug=True) 
