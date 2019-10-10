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
            password='pwguest{}'.format(n),
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("user", response.keys())


class UserAuthorizationTest(TestCase):

    def setUp(self):
        endpoint = get_api_endpoint('/user')
        data = dict(
            username='test',
            email='test@example.com',
            password='pwtest',
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)

    def test_can_create_a_user_authorization(self):
        endpoint = get_api_endpoint('/user/auth')
        data = dict(
            username='test',
            password='pwtest',
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("auth", response.keys())
