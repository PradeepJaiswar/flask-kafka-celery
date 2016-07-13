from flask_restful import Resource
from app.api import api

class UsersResource(Resource):
    def get(self):
        users = {
           '1' : "User 1",
           '2' : "User 2",
           '3' : "User 3",
        }
        return users,200

api.add_resource(UsersResource, '/users')
