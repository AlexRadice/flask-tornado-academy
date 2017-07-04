from flask import Flask, render_template

if __name__ == '__main__':
    app = Flask('flaskeg')

    @app.route('/')
    def index():
        "Home page"
        return render_template('index.html')

    app.run(port=11000, debug=True) 
