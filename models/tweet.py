from datetime import datetime
from .database import db


class Tweet(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    tag = db.Column(db.String(80), nullable=True)
    content = db.Column(db.String(255), nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow)

    user_id = db.Column(db.Integer, db.ForeignKey('user.id'), nullable=False)
    user = db.relationship('User', backref=db.backref('tweet', lazy=True))

    def __repr__(self):
        return "<Tweet from {} #{}: {}>".format(
            self.user_id, self.tag, self.content
        )
