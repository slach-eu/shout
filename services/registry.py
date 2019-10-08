class ServiceRegistry(object):

    registry = dict()

    def register(self, name, service_class):
        self.registry[name] = service_class

    def get(self, name, config={}):
        return self.registry.get(name)(config)
