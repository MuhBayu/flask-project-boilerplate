from flask import Flask
from flask_restful import Api
from controllers import indexController
from dotenv import load_dotenv
load_dotenv()

app = Flask(__name__)
api = Api(app)

api.add_resource(indexController.HelloWorld, '/')

if __name__ == '__main__':
    app.run(debug=True)