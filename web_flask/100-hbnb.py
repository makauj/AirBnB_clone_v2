#!/usr/bin/python3
"""Web flask application"""
from flask import Flask, render_template
from models import storage
from models.state import State
from models.amenity import Amenity

app = Flask(__name__)


@app.teardown_appcontext
def teardown():
    """Remove the running SQLAlchemy Session"""
    storage.close()


@app.route('/hbnb', strict_slashes=False)
def hbnb():
    """Display a HTML page: (inside the tag BODY)"""
    states = storage.all(State)
    amenities = storage.all(Amenity)
    return render_template('100-hbnb.html', states=states, amenities=amenities)


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
