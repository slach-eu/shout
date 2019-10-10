from flask import request
from flask_restful import Resource
from models.database import db
from models.user import User


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
        )
        db.session.add(user)
        db.session.commit()
        return {'user': repr(user)}
