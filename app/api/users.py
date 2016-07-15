from flask_restful import Resource
from app.api import api
from flask_restful_swagger import swagger

class UsersResource(Resource):
    "My USER API"
    @swagger.operation(
      notes='get a user list',
      nickname='get',
      # Parameters can be automatically extracted from URLs (e.g. <string:id>)
      # but you could also override them here, or add other parameters.
      parameters=[
          {
            "name": "user_id",
            "description": "The ID of user",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
          }
      ])
    def get(self):
        users = {
           '1' : "User 1",
           '2' : "User 2",
           '3' : "User 3",
        }
        return users,200

api.add_resource(UsersResource, '/users')
