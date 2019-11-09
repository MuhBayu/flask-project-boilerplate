import os
from flask_restful import Resource, Api
from flask import request

class HelloWorld(Resource):
    def get(self):
        id = os.getenv('APP_ID')
        print(id)
        return {'hello': 'world'}