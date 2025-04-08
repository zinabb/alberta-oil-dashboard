# THIS IS apps/authentication/__init__.py*

from flask import Blueprint

# Define the authentication blueprint
blueprint = Blueprint("authentication_blueprint", __name__, url_prefix="/auth")

# Import routes AFTER defining blueprint to avoid circular imports
from . import routes
