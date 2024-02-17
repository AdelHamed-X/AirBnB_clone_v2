#!/usr/bin/python3
""" A script that starts a Flask web application:
        Routes:
            /: display “Hello HBNB!”
            /hbnb: display “HBNB”
            /c/<text>:display “C” followed by the value of the text variable"""
from flask import Flask

app = Flask(__name__)


@app.route('/', strict_slashes=False)
def hello_hbnb():
    """ Returns: hello hbnb """
    return "Hello HBNB!"


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """ retruns: hbnb """
    return "HBNB"


@app.route('/c/<text>', strict_slashes=False)
def show_C(text):
    """ returns C ... """
    text = text.replace('_', ' ')
    return f"C {text}"


@app.route('/python', strict_slashes=False)
@app.route('/python/<string:text>', strict_slashes=False)
def show_python(text="is cool"):
    """ returns "Python" with default text """
    text = text.replace('_', ' ')
    return f"Python {text}"


@app.route('/number/<int:n>', strict_slashes=False)
def n_is_number(n):
    """ returns "n is a number" if it's only an integer """
    return f"{n} is a number"


if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5000)
