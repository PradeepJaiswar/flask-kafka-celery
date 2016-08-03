from flask_restful import reqparse, Resource
from app.api import api

from workers.worker1 import printNumbers
from random import randint

parser = reqparse.RequestParser()
parser.add_argument('url')

class UrlsResource(Resource):

    def post(self):
        args = parser.parse_args()
        #add celery job here
        printNumbers.delay()
        #for now make dummy response with post url parameters
        response = {
           'job_id' : randint(0,1000),
           'status' : "queued",
           'description' : 'Your crawling reuest for url ' + args.url + 'is accpeted',

        }
        return response,200

api.add_resource(UrlsResource, '/urls')
