#!/usr/bin/python3
""" A Flask script """

from models import *
from flask import Flask, render_template
from models.state import State

app = Flask(__name__)


@app.route('/states', strict_slashes=False)
@app.route('/states/<id>', strict_slashes=False)
def show_states(id=None):
    """ function to handle /states page """
    all_states = storage.all(State).values()
    if id is not None:
        all_states = storage.all(State)
        id = 'State.{}'.format(id)
    return render_template('9-states.html', all_states=all_states, id=id)


@app.teardown_appcontext
def teardown(exception):
    """ Reloading the session """
    storage.close()


if __name__ == '__main__':
    app.run(host="0.0.0.0", port=5000, debug=True)
