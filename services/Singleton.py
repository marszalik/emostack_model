class Singleton:
    _instances = {}

    def __init__(self, cls):
        self.cls = cls

    def __call__(self, *args, **kwargs):
        if self.cls not in Singleton._instances:
            Singleton._instances[self.cls] = self.cls(*args, **kwargs)
        return Singleton._instances[self.cls]