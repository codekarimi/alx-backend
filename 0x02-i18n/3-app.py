#!/usr/bin/env python3
"""
Flask Babel configuration
"""
import babel
from flask import Flask, render_template, request
from flask_babel import Babel, gettext

app = Flask(__name__)
babel = Babel(app)


class Config:
    """
    Config class for Babel
    """
    LANGUAGES = ["en", "fr"]
    BABEL_DEFAULT_LOCALE = "en"
    BABEL_DEFAULT_TIMEZONE = "UTC"


app.config.from_object(Config)
app.jinja_env.add_extension('jinja2.ext.i18n')


def get_locale():
    """
    Get locale from request
    """
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template('3-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run(debug=True)
