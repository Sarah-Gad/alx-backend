#!/usr/bin/env python3
"""This mudule setup a falsk app"""
from flask import Flask
from flask import render_template


app = Flask(__name__)


@app.route("/")
def home():
    """This is the home page"""
    return render_template("index.html")


if __name__ == "__main__":
    app.run(debug=True)
