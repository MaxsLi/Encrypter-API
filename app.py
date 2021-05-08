# -*- coding: utf-8 -*-

"""
A REST API for encrypting and decrypting inputs.
"""

from flask import Flask
from flask_restful import Resource, Api, abort
from httpimport import github_repo

# Importing Encrypter remotely from GitHub
with github_repo(username='MaxsLi', repo='Encrypter', module='ED'):
    import ED

__author__ = "Shangru Li"
__copyright__ = "Copyright 2021, Shangru Li"
__credits__ = "Shangru Li"
__license__ = "MIT"
__version__ = "1.0"
__maintainer__ = "Shangru Li"
__email__ = "maxsli@protonmail.com"
__status__ = "Stable"

app = Flask(__name__)
api = Api(app)


class Encrypt(Resource):
    def encrypt(self, text):
        try:
            return ED.encrypt(text)
        except SyntaxError as error:
            abort(400, message=error)

    def post(self, text):
        return {
                   'result': self.encrypt(text)
               }, 201


class Decrypt(Resource):
    def decrypt(self, cypher):
        try:
            return ED.decrypt(cypher)
        except SyntaxError as error:
            abort(400, message=error)

    def post(self, cypher):
        return {
                   'result': self.decrypt(cypher)
               }, 201


# adding the defined resources along with their corresponding urls
api.add_resource(Encrypt, '/encrypt/<text>')
api.add_resource(Decrypt, '/decrypt/<cypher>')

if __name__ == '__main__':
    app.run()
