# -*- coding: utf-8 -*-

"""
A REST API for encrypting and decrypting inputs.
"""

from flask import Flask
from flask_restful import reqparse, Resource, Api, abort
from flask_cors import CORS
from httpimport import github_repo

# Importing Encrypter remotely from GitHub
with github_repo(username='MaxsLi', repo='Encrypter', module='ED'):
    import ED

__author__ = "Shangru Li"
__copyright__ = "Copyright 2021, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "1.3"
__maintainer__ = "Shangru Li"
__email__ = "maxsli@protonmail.com"
__status__ = "Stable"

app = Flask(__name__)
api = Api(app)
CORS(app)

parser = reqparse.RequestParser()
parser.add_argument('input', type=str, help='Input as a text or cypher')


class Ping(Resource):
    def get(self):
        return {"status": "ok", "version": __version__}, 200


class Encrypt(Resource):
    def encrypt(self, text):
        try:
            return ED.encrypt(text)
        except SyntaxError as error:
            abort(400, error=error.msg)

    def post(self):
        args = parser.parse_args()
        if args.input is None:
            abort(400, error="Please provide a text to encrypt.")
        else:
            return {'result': self.encrypt(args.input)}, 200


class Decrypt(Resource):
    def decrypt(self, cypher):
        try:
            return ED.decrypt(cypher)
        except SyntaxError as error:
            abort(400, error=error.msg)

    def post(self):
        args = parser.parse_args()
        if args.input is None:
            abort(400, error="Please provide a cypher to decrypt.")
        else:
            return {'result': self.decrypt(args.input)}, 200


# adding the defined resources along with their corresponding urls
api.add_resource(Ping, '/', '/ping')
api.add_resource(Encrypt, '/encrypt')
api.add_resource(Decrypt, '/decrypt')

if __name__ == '__main__':
    app.run()
