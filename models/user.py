from .database import db


class User(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    username = db.Column(db.String(80), unique=True, nullable=False)
    email = db.Column(db.String(120), unique=True, nullable=False)
    password = db.Column(db.String(255), nullable=False)

    def __repr__(self):
        return '<User %r>' % self.username


class UserAuthorization(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    token = db.Column(db.String(8), unique=True, nullable=False)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('auth', lazy=True))

    def __repr__(self):
        return "<Authorization for user {}>".format(self.user_id)
