#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel, Locale


app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """ Config class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


@babel.localeselector
def get_locale():
    """ Get locale from request """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


app.config.from_object(Config)


@app.route('/')
def index() -> str:
    """ GET /
    Return:
      - Render template
    """
    return render_template('2-index.html')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port='3000')
