from flask_restful import Resource
from app.api import api
from flask_restful_swagger import swagger

class CustomersResource(Resource):
    "My CUSTOMER API"
    @swagger.operation(
      notes='get a customer list',
      nickname='get',
      # Parameters can be automatically extracted from URLs (e.g. <string:id>)
      # but you could also override them here, or add other parameters.
      parameters=[
          {
            "name": "customer_id",
            "description": "The ID of customer",
            "required": True,
            "allowMultiple": False,
            "dataType": 'string',
          }
      ])
    def get(self):
        customers = {
           '1' : "customer 1",
           '2' : "customer 2",
           '3' : "customer 3",
        }
        return customers,200

api.add_resource(CustomersResource, '/customers')
