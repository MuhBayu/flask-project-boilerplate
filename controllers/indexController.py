from flask_restful import Resource
from flask import request

class HelloWorld(Resource):
    def get(self):
        return {'status': 200}