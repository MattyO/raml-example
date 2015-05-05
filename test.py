import unittest
import pyraml.parser
import jsonschema
import requests


class ApiTests(unittest.TestCase):
    @classmethod
    def setUpClass(self):
        self.parser = pyraml.parser.load('spec.raml')

    def test_something(self):
        #print self.parser
        schema =self.parser.resources['/'].methods['get'].responses[200].body['application/json'].schema
        jsonschema.validate(requests.get('http://localhost:5000').json(), schema)

