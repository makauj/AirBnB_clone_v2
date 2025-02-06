#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n=None):
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", n=n)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n=None):
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number/<n>", strict_slashes=False)
def nums(n):
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    return "Python {}".format(text.replace("_", " "))


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    return "C {}".format(text.replace("_", " "))


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello():
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
