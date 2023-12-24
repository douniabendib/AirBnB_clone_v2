#!/usr/bin/python3
"""
script that start flask application
"""

from flask import Flask
app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """return hello hbnb"""
    return f"Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """return hbnb"""
    return f"HBNB"


@app.route('/c/<text>', strict_slashes=False)
def c_index(text):
    """return c followed by the value of text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_index(text='is cool'):
    """return python followed by the value text"""
    return f"Python {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
