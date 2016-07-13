from flask_restful import Resource
from app.api import api

class CustomersResource(Resource):
    def get(self):
        customers = {
           '1' : "customer 1",
           '2' : "customer 2",
           '3' : "customer 3",
        }
        return customers,200

api.add_resource(CustomersResource, '/customers')        
