#!/usr/bin/env python3
""" Basic Flask app """
from flask import Flask, render_template, request
from flask_babel import Babel


class Config(object):
    """ Config class for Babel """
    LANGUAGES = ['en', 'fr']
    BABEL_DEFAULT_LOCALE = 'en'
    BABEL_DEFAULT_TIMEZONE = 'UTC'


app = Flask(__name__)
app.config.from_object(Config)
babel = Babel(app)


@babel.localeselector
def get_locale() -> str:
    """ Get locale from request """
    language = request.args.get('locale')
    if language and language in app.config['LANGUAGES']:
        return language
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index() -> str:
    """ GET /
    Return:
      - Render template
    """
    return render_template('4-index.html')


if __name__ == '__main__':
    """ Main Function """
    app.run(host='0.0.0.0', port='3000')
