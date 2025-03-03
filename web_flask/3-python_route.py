#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/python/<text>", strict_slashes=False)
def python(text):
    """display Python followed by the value of the text variable"""
    return f"Python {text.replace("_", "")}"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """display C followed by the value of the text variable"""
    return f"C {text.replace("_", " ")}"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """hbnb route"""
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello():
    """hello route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
