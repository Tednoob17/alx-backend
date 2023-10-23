#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request, g
from flask_babel import Babel


class Config(object):
    """ Config class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)
users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request """
    language = request.args.get('locale', '')
    if language and language in app.config['LANGUAGES']:
        return language
    if g.user and g.user.get('locale') in app.config['LANGUAGES']:
        return g.user.get('locale')
    header_lang = request.headers.get('locale', '')
    if header_lang and header_lang in app.config['LANGUAGES']:
        return header_lang
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(login_as: int) -> dict:
    """ Get user from dict """
    id = request.args.get('login_as')
    if id and int(id) in users:
        return users.get(int(id))
    return None


@app.before_request
def before_request() -> None:
    """ Before request handler """
    user = get_user(request.args.get('login_as'))
    if user:
        g.user = user


@app.route('/')
def index() -> str:
    """ GET /
    Return:
      - Render template
    """
    return render_template('6-index.html')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port='3000')
