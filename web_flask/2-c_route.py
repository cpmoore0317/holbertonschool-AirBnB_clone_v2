#!/usr/bin/python3
""" A script that starts a Flask web app, adding a C display route """

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnbL():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # Replace underscores with spaces
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)