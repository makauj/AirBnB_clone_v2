#!/usr/bin/python3
"""Python script that starts a Flask web application"""
from flask import Flask, render_template


app = Flask(__name__)


@app.route("/number_odd_or_even/<n>", strict_slashes=False)
def number_odd_or_even(n=None):
    """number_odd_or_even route"""
    if isinstance(n, int):
        return render_template("6-number_odd_or_even.html", n=n)


@app.route("/number_template/<n>", strict_slashes=False)
def number_template(n=None):
    """Display a HTML page only if n is an integer"""
    if isinstance(n, int):
        return render_template("5-number.html", n=n)


@app.route("/number/<n>", strict_slashes=False)
def nums(n):
    """determine if n is a number"""
    if isinstance(n, int):
        return f"{n} is a number"


@app.route("/python/<text>", strict_slashes=False)
def display_python(text):
    """Dispaly Python followed by the value of the text variable"""
    return "Python {}".format(text.replace("_", " "))


@app.route("/c/<text>", strict_slashes=False)
def display_c(text):
    """Display C followed by the value of the text variable"""
    return "C {}".format(text.replace("_", " "))


@app.route("/hbnb", strict_slashes=False)
def hbnb():
    """HBNB route"""
    return "HBNB"


@app.route("/", strict_slashes=False)
def hello():
    """Hello route"""
    return "Hello HBNB!"


if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000, debug=None)
