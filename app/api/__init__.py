from flask import Blueprint
from flask_restful import Api

api_blueprint = Blueprint("api", __name__, url_prefix='/api')
api = Api(api_blueprint)

# Import the resources to add the routes to the blueprint before the app is
# initialized
from . import users  # NOQA
from . import customers  # NOQA
