from flask_restful import Resource
from models.tweet import Tweet


class TweetResource(Resource):

    def get(self, tweet_id):
        tweet = Tweet.query.get(tweet_id)
        return {
            'tag': '#{}'.format(tweet.tag),
            'tweet': '{}'.format(tweet.content),
        }
