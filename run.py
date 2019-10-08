#!/usr/bin/env python
from random import randint
from flask import jsonify
from services import config
from services import registry
from models.database import db
from models.user import User


service = registry.get("application_service", config)
app = service.get_app()


@app.route('/api/users', methods=['GET'])
def get_users():
    n = randint(100, 100*100)
    user = User(
        username='guest{}'.format(n),
        email='guest{}@example.com'.format(n),
    )
    db.session.add(user)
    db.session.commit()
    users = User.query.all()
    return jsonify({'users': [repr(x) for x in users]})


def run_app():
    db.init_app(app)
    with app.app_context():
        db.create_all()
        db.session.commit()
    app.run(debug=True)


if __name__ == '__main__':
    run_app()
