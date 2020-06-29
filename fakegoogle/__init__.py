from flask import Flask

def create_app():

    app = Flask(__name__)

    from . import webapp
    app.register_blueprint(webapp.blueprint)

    return app