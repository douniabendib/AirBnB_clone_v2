#!/usr/bin/python3
"""
script that start flask apllication
"""

from flask import Flask, render_template
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
    """return c followed by the value text"""
    return f"C {text.replace('_', ' ')}"


@app.route('/python', strict_slashes=False)
@app.route('/python/(<text>)', strict_slashes=False)
def python_index(text='is cool'):
    """return python followed by the value text"""
    return f"Python {text.replace('_', ' ')}"


@app.route('/number/<int:n>', strict_slashes=False)
def numb(n):
    """return n"""
    return f"{n} is a number"


@app.route('/number_template/<int:n>', strict_slashes=False)
def num_temp(n):
    """display a HTML page"""
    return render_template('5-number.html', n=n)


@app.route('/number_odd_or_even/<int:n>', strict_slashes=False)
def add_even(n):
    """dislay add or even """
    if n % 2 == 0:
        even_odd = 'even'
    else:
        even_odd = 'odd'
    return render_template('6-number_odd_or_even.html', n=n, even_odd=even_odd)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port='5000')
