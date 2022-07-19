#!/usr/bin/env python3
"""Defines a basic flask app
Configures available languages for i18n
"""

from flask import Flask, render_template
from flask_babel import Babel

app = Flask(__name__)
babel = Babel(app)


class Config(object):
    """Configures available languages in the flask app
    """
    LANGUAGES = ["en", "fr"]


app.config.from_object('1-app.Config')


@app.route("/")
def index() -> str:
    """Renders an html document
    """
    return render_template('1-index.html')


if __name__ == "__main__":
    app.run(debug=True)
