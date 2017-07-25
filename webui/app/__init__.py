from flask import Flask

from app import config


def configure_app(app):
    app.config.from_object(config)


def add_views(_app):
    from app.views import IndexView

    _app.add_url_rule('/', view_func=IndexView.as_view('index'))


def create_app():
    app = Flask(__name__)
    configure_app(app)
    add_views(app)
    return app