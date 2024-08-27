#!/usr/bin/env python3
''' Flask base module'''

from flask import Flask, request, g
import flask
from flask_babel import Babel
from typing import Union

app = Flask(__name__, template_folder='templates')
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config(object):
    ''' config babel'''
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_TIMEZONE = 'UTC'
    BABEL_DEFAULT_LOCALE = 'en'


app.config.from_object(Config)


@babel.localeselector
def get_locale() -> str:
    """ get locale selector to guess user accept language """
    locale = request.args.get("locale")
    if locale and locale in app.config['LANGUAGES']:
        return locale
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user() -> Union[dict, None]:
    """ returns a user dictionary of none if ID cannot no found"""
    try:
        login = request.args.get('login_as')
        user = users[int(login)]
    except Exception:
        user = None

    return user


@app.before_request
def before_request():
    """ before request for user"""
    user = get_user()
    g.user = user


@app.route("/", methods=['GET'], strict_slashes=False)
def hello_world() -> str:
    """ return 0-index template"""
    return flask.render_template('5-index.html')


if __name__ == "__main__":
    app.run()
