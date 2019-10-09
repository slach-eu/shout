from flask_restful import Resource
from models.user import User


class UserResource(Resource):

    def get(self, user_id):
        user = User.query.get(user_id)
        return {'hello': 'user {}'.format(user.username)}
