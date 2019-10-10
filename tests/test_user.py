import requests
from unittest import TestCase
from .helpers import get_api_endpoint


class UserTest(TestCase):

    def test_can_obtain_a_user(self):
        endpoint = get_api_endpoint('/user/{}'.format(1))
        req = requests.get(endpoint)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("user", response.keys())

    def test_can_create_a_user(self):
        endpoint = get_api_endpoint('/user')
        data = {"key": "value"}
        req = requests.post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("user", response.keys())
