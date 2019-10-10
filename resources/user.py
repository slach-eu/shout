from flask import request
from flask_restful import Resource
from sqlalchemy.orm.exc import NoResultFound

from models.database import db
from models.user import User, UserAuthorization
from models.helpers import get_password_hash
from models.helpers import generate_random_token


class UserResource(Resource):

    def get(self, user_id):
        user = User.query.get(user_id)
        return {'user': repr(user)}


class UsersResource(Resource):

    def post(self):
        if not request.is_json:
            raise Exception()

        content = request.get_json()
        user = User(
            username=content['username'],
            email=content['email'],
            password=get_password_hash(content['password']),
        )
        db.session.add(user)
        db.session.commit()
        return {'user': repr(user)}


class UserAuthorizationsResource(Resource):

    def post(self):
        if not request.is_json:
            raise Exception()

        content = request.get_json()

        try:
            user = User.query.filter_by(username=content['username']).one()
        except NoResultFound as e:
            raise Exception("No user found")

        password = get_password_hash(content['password'])
        if user.password != password:
            raise Exception("Invalid password")

        UserAuthorization.query.filter_by(user=user).delete()

        auth = UserAuthorization(
            user_id=user.id,
            token=generate_random_token(),
        )
        db.session.add(auth)
        db.session.commit()
        return {'auth': auth.dict()}
