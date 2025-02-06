#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask


app = Flask(__name__)


@app.route("/number/<n>", strict_slashes=False)
def nums(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    return f"Python {text.replace("_", "")}"


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    return f"C {text.replace("_", " ")}"


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
