#!/usr/bin/env python3
"""Task 1 Module"""
from flask import Flask, render_template, request, g
from typing import Union, Dict
from flask_babel import Babel

users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


def get_user() -> Union[Dict, None]:
    """This fucntio return the user dict"""
    login_id = request.args.get("login_as")
    if login_id:
        return users.get(int(login_id))
    return None


class Config:
    """This class represents the falsk config"""
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@app.before_request
def before_request() -> None:
    """Performs some routines before each request's resolution."""
    user = get_user()
    g.user = user


@babel.localeselector
def get_locale():
    """this fucntion will get the best language match"""
    queries = request.query_string.decode('utf-8').split('&')
    query_table = dict(map(
        lambda x: (x if '=' in x else '{}='.format(x)).split('='),
        queries,
    ))
    if 'locale' in query_table:
        if query_table['locale'] in app.config["LANGUAGES"]:
            return query_table['locale']
    return request.accept_languages.best_match(app.config["LANGUAGES"])


@app.route("/")
def home():
    """This is the home page"""
    return render_template("5-index.html")


if __name__ == "__main__":
    app.run(debug=True)
