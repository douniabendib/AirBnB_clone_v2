#!/usr/bin/python3
"""
script that start flask app
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
    """return C followed by the value text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<text>', strict_slashes=False)
def python_index(text='is cool'):
    """return python followed by the value of text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    """return number"""
    return f"{n} is a number"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
