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


@babel.localeselector
def get_locale():
    """
    Get locale from request
    """
    if request.args.get('locale') \
            and request.args.get('locale') in app.config['LANGUAGES']:
        return request.args.get('locale')
    return request.accept_languages.best_match(app.config['LANGUAGES'])


@app.route('/')
def index():
    """
    Render the index page
    """
    home_title = gettext("home_title")
    home_header = gettext("home_header")
    return render_template('4-index.html', home_title=home_title,
                           home_header=home_header)


if __name__ == '__main__':
    app.run(debug=True, host="0.0.0.0", port="5000")
