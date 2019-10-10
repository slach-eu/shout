from flask import request
from flask_restful import Resource
from sqlalchemy.orm.exc import NoResultFound

from models.tweet import Tweet
from models.user import User, UserAuthorization
from models.database import db


class TweetResource(Resource):

    def get(self, tweet_id):
        tweet = Tweet.query.get(tweet_id)
        return {
            'tag': '#{}'.format(tweet.tag),
            'tweet': '{}'.format(tweet.content),
        }


class TweetsResource(Resource):

    def get(self):
        tweets = Tweet.query.all()
        return {
            'tweets': [repr(t) for t in tweets],
        }

    def post(self):
        if not request.is_json:
            raise Exception()

        content = request.get_json()

        try:
            user = User.query.filter_by(username=content['username']).one()
        except NoResultFound as e:
            raise Exception("No user found")

        try:
            auth = UserAuthorization.query.filter_by(user_id=user.id).one()
        except NoResultFound as e:
            raise Exception("Request unauthorized")

        if auth.token != content['token']:
            raise Exception("Invalid token")

        tweet = Tweet(
            user=user,
            content=content['content'],
            tag=content['tag'],
        )
        db.session.add(tweet)
        db.session.commit()

        return {'tweet': repr(tweet)}
