#!/usr/bin/python3
"""
scrpit for start flask application
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
    """return c plus text"""
    return f"C {text.replace('_', ' ')}"

if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
