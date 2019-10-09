#!/usr/bin/env python
from random import randint
from flask import jsonify
from flask_restful import Api
from models.tweet import Tweet
from services import config
from services import registry
from models.database import db
from models.user import User
from resources.user import UserResource
from resources.tweet import TweetResource


service = registry.get("application_service", config)
app = service.get_app()
api = Api(app)


@app.route('/api/tweets', methods=['GET'])
def get_tweets():
    n = randint(100, 100*100)
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
    return jsonify({'tweets': [repr(t) for t in tweets]})


def run_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)


api.add_resource(UserResource, '/api/user/<user_id>')
api.add_resource(TweetResource, '/api/tweet/<tweet_id>')

if __name__ == '__main__':
    run_app()
