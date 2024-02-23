#!/usr/bin/python3
""" A flask script """

from flask import Flask, render_template
from models import *
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def app_teardown(exception):
    storage.close()

@app.route('/states_list', strict_slashes=False)
def states_list():
    all_states = storage.all(State).values()
    return render_template('7-states_list.html', all_states=all_states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)
