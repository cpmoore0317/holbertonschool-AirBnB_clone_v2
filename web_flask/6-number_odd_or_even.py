#!/usr/bin/python3
""" A script that starts a Flask web application, route for hmtl display """
from flask import Flask, render_template

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    return 'Hello HBNB!'


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'


@app.route('/c/<text>', strict_slashes=False)
def c_route(text):
    # Replace underscores with spaces
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)


@app.route('/python/', defaults={'text': 'is cool'}, strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_route(text):
    # Replace underscores with spaces
    display_text = text.replace('_', ' ')
    return 'Python {}'.format(display_text)


@app.route('/number/<int:n>', strict_slashes=False)
def number_route(n):
    return '{} is a number'.format(n)


@app.route('/number_template/<int:n>', strict_slashes=False)
def number_template_route(n):
    return render_template('5-template.html', number=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def odd_or_even_route(n):
    return(render_template('6-number_odd_or_even.html', n=n))


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
