from flask import Flask


class ApplicationService(object):

    app = None
    config = {
        'SQLALCHEMY_DATABASE_URI': 'sqlite://',
    }

    def __init__(self, config=None):
        self.config.update(config)

    def get_app(self):
        if self.app is None:
            self.app = Flask(__name__)
            self.app.config.update(self.config)

        return self.app
