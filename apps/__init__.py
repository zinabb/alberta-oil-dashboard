# THIS IS apps/__init__.py

from flask import Flask
from flask_login import LoginManager
from flask_sqlalchemy import SQLAlchemy
from importlib import import_module


db = SQLAlchemy()
login_manager = LoginManager()


def register_extensions(app):
    db.init_app(app)
    login_manager.init_app(app)


def register_blueprints(app):
    from apps.authentication import blueprint as auth_blueprint
    from apps.home import blueprint as home_blueprint

    # Keep the auth prefix for authentication
    app.register_blueprint(auth_blueprint, url_prefix="/auth")

    # Register the home blueprint with NO prefix
    app.register_blueprint(home_blueprint)


def configure_database(app):

    @app.before_first_request
    def initialize_database():
        db.create_all()

    @app.teardown_request
    def shutdown_session(exception=None):
        db.session.remove()

from apps.authentication.oauth import github_blueprint

def create_app(config):
    app = Flask(__name__)
    print("Registered Blueprints BEFORE:", app.blueprints.keys())  # Debugging print statement
    app.config.from_object(config)
    
    register_extensions(app)  # Initialize DB & login manager
    register_blueprints(app)  # Registers the home and authentication blueprints
    app.register_blueprint(github_blueprint, url_prefix="/login")
   #f app.register_blueprint(home_blueprint)  # no url_prefix

    configure_database(app)
    
    print("Registered Blueprints AFTER:", app.blueprints.keys())  # Debugging print statement
    return app

