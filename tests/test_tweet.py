from unittest import TestCase
from requests import get, post
from .helpers import get_api_endpoint


class TweetTest(TestCase):

    def setUp(self):
        endpoint = get_api_endpoint('/user')
        data = dict(
            username='test',
            email='test@example.com',
            password='pwtest',
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)

    def test_can_create_a_tweet(self):
        endpoint = get_api_endpoint('/user/auth')
        data = dict(
            username='test',
            password='pwtest',
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn('auth', response.keys())
        token = response['auth']['token']

        endpoint = get_api_endpoint('/tweet')
        data = dict(
            username='test',
            token=token,
            content='lorem ipsum',
            tag='lorem',
        )
        req = post(endpoint, json=data)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("tweet", response.keys())


class TweetByTagTest(TestCase):

    def test_can_obtain_tweets_by_tag(self):
        endpoint = get_api_endpoint('/tweet/tag/{}'.format('lorem'))
        req = get(endpoint)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("tweets", response.keys())
        self.assertIn("page", response.keys())
        self.assertIn("count", response.keys())


class TweetByDate(TestCase):

    def test_can_obtain_tweets_by_date(self):
        endpoint = get_api_endpoint(
            '/tweet/by_date/{}/{}'.format('2000-01-01', '2222-02-02')
        )
        req = get(endpoint)
        self.assertTrue(req.status_code, 200)
        response = req.json()
        self.assertIn("tweets", response.keys())
        self.assertIn("page", response.keys())
        self.assertIn("count", response.keys())
