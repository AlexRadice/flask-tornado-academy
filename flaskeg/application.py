from flask import Flask, render_template

if __name__ == '__main__':
    developers = [{
        'name': 'Alex Radice',
        'cell': 'A',
        'favourite_fruit': 'grapefruit'
        }]
    app = Flask('flaskeg')

    @app.route('/')
    def index():
        "Home page"
        return render_template('index.html', developers=developers)

    app.run(port=11000, debug=True) 
