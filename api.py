'''
Simple REST Server
Receive a filename as parameter and response a message as the processing procedure.
'''

from flask import Flask, request
from flask_restful import Resource, Api

app = Flask(__name__)
api = Api(app)

class HelloWorld(Resource):
    def get(self):
        return {'responseMessageFromGet':'hello world'}
    def put(self):
        filename = request.form['filename']  # corresponding to the filename uploaded from client
        print filename
        msgResp = filename + ' has been proccessed'
        return {'responseMessageFromPut':msgResp}

api.add_resource(HelloWorld, '/')

if __name__=='__main__':
    app.run(debug=True)
