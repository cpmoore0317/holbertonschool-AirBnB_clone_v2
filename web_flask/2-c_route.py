#!/usr/bin/python3

from flask import Flask

app = Flask(__name__)

@app.route('/', strict_slashes=False)
def hello_hbnbL():
    return 'Hello HBNB!'

@app.route('/hbnb', strict_slashes=False)
def hbnb():
    return 'HBNB'

def c_route(text):
    # Replace underscores with spaces
    display_text = text.replace('_', ' ')
    return 'C {}'.format(display_text)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)