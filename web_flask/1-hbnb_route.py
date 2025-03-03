#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB route"""
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello():
    """hello route
    Return (str): Hello HBNB!
    """
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
