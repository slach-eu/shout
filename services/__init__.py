from .registry import ServiceRegistry
from .application import ApplicationService


config = {
    'SQLALCHEMY_DATABASE_URI': 'sqlite:///C:\\slach\\database.db',
    'SQLALCHEMY_TRACK_MODIFICATIONS': False,
}


registry = ServiceRegistry()
registry.register("application_service", ApplicationService)
