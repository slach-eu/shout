from unittest import TestCase
from random import randint
from requests import get, post
from .helpers import get_api_endpoint


class UserTest(TestCase):

    def test_can_obtain_a_user(self):
        endpoint = get_api_endpoint('/user/{}'.format(1))
        req = get(endpoint)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("user", response.keys())

    def test_can_create_a_user(self):
        endpoint = get_api_endpoint('/user')
        n = randint(100, 100 * 100)
        data = dict(
            username='guest{}'.format(n),
            email='guest{}@example.com'.format(n),
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("user", response.keys())
