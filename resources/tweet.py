from datetime import datetime
from flask import request
from flask_restful import Resource, abort
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
            abort(400, message="Could not parse JSON")

        content = request.get_json()

        try:
            user = User.query.filter_by(
                username=content['username']
            ).one()
        except NoResultFound as e:
            abort(401, message="No user found")

        try:
            auth = UserAuthorization.query.filter_by(
                user_id=user.id
            ).one()
        except NoResultFound as e:
            abort(401, message="No user authorization found")

        if auth.token != content['token']:
            abort(403, message="Invalid token found")

        tweet = Tweet(
            user=user,
            content=content['content'],
            tag=content['tag'],
        )
        db.session.add(tweet)
        db.session.commit()

        return {'tweet': repr(tweet)}


class TweetsTagResource(Resource):

    def get(self, tag, limit=10):
        try:
            page = int(request.args.get("page", 1)) - 1
        except ValueError as e:
            abort(400, details="Could not parse page argument")

        query = Tweet.query.filter_by(tag=tag)
        count = query.count()

        tweets = query.limit(limit).offset(limit*page).all()

        return {
            'tweets': [repr(t) for t in tweets],
            'count': count,
            'page': page,
        }


class TweetsByDateResource(Resource):

    def get(self, begin, end, limit=10):
        try:
            page = int(request.args.get("page", 1)) - 1
        except ValueError as e:
            abort(400, details="Could not parse page argument")

        begin_date = datetime.strptime(begin, "%Y-%m-%d")
        end_date = datetime.strptime(end, "%Y-%m-%d")
        query = Tweet.query\
            .filter(Tweet.created_at >= begin_date)\
            .filter(Tweet.created_at <= end_date)
        count = query.count()

        tweets = query.limit(limit).offset(limit*page).all()

        return {
            'tweets': [repr(t) for t in tweets],
            'count': count,
            'page': page,
            'begin': begin,
            'end': end,
        }
