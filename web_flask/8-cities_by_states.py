#!/usr/bin/python3
'''
Script that starts a Flask web application and displays the states
and cities objects sorted alphabetically form A->Z
'''
from models import storage
from models import *
from flask import Flask, render_template

app = Flask(__name__)


@app.route("/cities_by_states", strict_slashes=False)
def cities_by_states():
    '''Returns the states and cities list sorted in A->Z'''
    states = storage.all("State").values()
    return render_template('8-cities_by_states.html', states=states)


@app.teardown_appcontext
def close_database(err):
    '''Closes all the sqlalchemy of the database'''


if __name__ == "__main__":
    app.run(host='0.0.0.0', port=5000)
