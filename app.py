# -*- coding: utf-8 -*-

"""
A REST API for encrypting and decrypting inputs.
"""

from flask import Flask
from flask_restful import reqparse, Resource, Api, abort
from httpimport import github_repo

# Importing Encrypter remotely from GitHub
with github_repo(username='MaxsLi', repo='Encrypter', module='ED'):
    import ED

__author__ = "Shangru Li"
__copyright__ = "Copyright 2021, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "1.1"
__maintainer__ = "Shangru Li"
__email__ = "maxsli@protonmail.com"
__status__ = "Stable"

app = Flask(__name__)
api = Api(app)

parser = reqparse.RequestParser()
parser.add_argument('input', type=str, help='Input as a text or cypher')


class Encrypt(Resource):
    def encrypt(self, text):
        try:
            return ED.encrypt(text)
        except SyntaxError as error:
            abort(400, message=error.msg)

    def post(self):
        args = parser.parse_args()
        if args.input is None:
            abort(400, message="Please provide a text to encrypt.")
        else:
            return {'result': self.encrypt(args.input)}, 201


class Decrypt(Resource):
    def decrypt(self, cypher):
        try:
            return ED.decrypt(cypher)
        except SyntaxError as error:
            abort(400, message=error.msg)

    def post(self):
        args = parser.parse_args()
        if args.input is None:
            abort(400, message="Please provide a cypher to decrypt.")
        else:
            return {'result': self.decrypt(args.input)}, 201


# adding the defined resources along with their corresponding urls
api.add_resource(Encrypt, '/encrypt')
api.add_resource(Decrypt, '/decrypt')

if __name__ == '__main__':
    app.run()
