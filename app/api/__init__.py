from flask import Blueprint
from flask_restful import Api
from flask_restful_swagger import swagger

api_blueprint = Blueprint("api", __name__, url_prefix='/v1/api')
# api = Api(api_blueprint)

###################################
# Wrap the Api with swagger.docs. It is a thin wrapper around the Api class that adds some swagger smarts
# api = swagger.docs(Api(api_blueprint), apiVersion='0.1')
###################################


###################################
# This is important:
api = swagger.docs(Api(api_blueprint), apiVersion='0.1',
                   basePath='http://localhost:5000',
                   resourcePath='/',
                   produces=["application/json", "text/html"],
                   api_spec_url='/docs/spec',
                   description='Blueprint1 Description')
###################################



# Import the resources to add the routes to the blueprint before the app is
# initialized
from . import users  # NOQA
from . import customers  # NOQA
