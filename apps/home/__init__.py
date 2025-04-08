# THIS IS apps/home/__init__.py*

from flask import Blueprint

# Define the Blueprint
blueprint = Blueprint("home_blueprint", __name__, url_prefix="")

# Import routes AFTER defining the blueprint to avoid circular imports
from . import routes
