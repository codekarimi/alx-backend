#!/usr/bin/env python3
"""
Flask Babel configuration
"""
import babel
from flask import Flask, render_template, request, g
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


users = {
    1: {"name": "Balou", "locale": "fr", "timezone": "Europe/Paris"},
    2: {"name": "Beyonce", "locale": "en", "timezone": "US/Central"},
    3: {"name": "Spock", "locale": "kg", "timezone": "Vulcan"},
    4: {"name": "Teletubby", "locale": None, "timezone": "Europe/London"},
}


class Config:
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.jinja_env.add_extension('jinja2.ext.i18n')


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    if request.args.get('locale') \
            and request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


def get_user(id: int = None) -> dict:
    """
    Get users from url parameter
    """
    if id is None:
        return None
    return users.get(int(id))


@app.before_request
def before_request():
    """
    Find a user if any, and set it as a global on `g.user`
    """
    g.user = get_user(request.args.get('login_as'))


@app.route('/')
def index():
    """
    Render the index page
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template('5-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
