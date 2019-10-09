from random import randint
from flask_restful import Resource
from models.tweet import Tweet
from models.user import User
from models.database import db


class TweetResource(Resource):

    def get(self, tweet_id):
        tweet = Tweet.query.get(tweet_id)
        return {
            'tag': '#{}'.format(tweet.tag),
            'tweet': '{}'.format(tweet.content),
        }

    def post(self):
        n = randint(100, 100 * 100)
        user = User(
            username='guest{}'.format(n),
            email='guest{}@example.com'.format(n),
        )
        db.session.add(user)
        tweet = Tweet(
            content='Some shitty tweet',
            tag='shit',
            user=user,
        )
        db.session.add(tweet)
        db.session.commit()
        tweets = Tweet.query.all()
        return {'tweets': [repr(t) for t in tweets]}
