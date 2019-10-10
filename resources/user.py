from random import randint
from flask_restful import Resource
from models.database import db
from models.user import User


class UserResource(Resource):

    def get(self, user_id):
        user = User.query.get(user_id)
        return {'user': repr(user)}


class UsersResource(Resource):

    def post(self):
        n = randint(100, 100 * 100)
        user = User(
            username='guest{}'.format(n),
            email='guest{}@example.com'.format(n),
        )
        db.session.add(user)
        db.session.commit()
        return {'user': repr(user)}
