#!/usr/bin/env python
from flask_restful import Api
from services import config
from services import registry
from models.database import db
from resources.user import UserResource, UsersResource
from resources.user import UserAuthorizationsResource
from resources.tweet import TweetResource, TweetsResource
from resources.tweet import TweetsTagResource


# configure application
service = registry.get("application_service", config)
app = service.get_app()

# configure api
api = Api(app)
api.add_resource(UsersResource, '/api/user')
api.add_resource(UserResource, '/api/user/<user_id>')
api.add_resource(UserAuthorizationsResource, '/api/user/auth')
api.add_resource(TweetsResource, '/api/tweet')
api.add_resource(TweetResource, '/api/tweet/<tweet_id>')
api.add_resource(TweetsTagResource, '/api/tweet/tag/<tag>')


if __name__ == '__main__':
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)
