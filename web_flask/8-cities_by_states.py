#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models.state import State


app = Flask(__name__)


@app.teardown_appcontext
def teardown(self):
    """Close current SQLAlchemy session"""
    storage.close()


@app.route("/cities_by_states", strict_slashes=False)
def state_list():
    """Display a HTML page with a list of all States"""
    states = storage.all(State)
    return render_template('8-states_list.html', states=states)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
