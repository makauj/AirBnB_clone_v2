#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template
from models import storage
from models import State


app = Flask()


@app.route("/states")
def state_list():
    """Display a HTML page with a list of all States"""
    states = storage.all(State)
    return render_template('7-states_list.html', states=states)


@app.teardown_appcontext
def teardown(self):
    """Close current SQLAlchemy session"""
    storage.close()


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
