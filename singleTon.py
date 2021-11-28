class Singleton(object):
    _instance = {}

    def __init__(cls, *args, **kwargs):
        if cls not in cls._instance:
            instance = super().__init__(*args, **kwargs)
            cls._instance[cls] = instance

        return cls._instance[cls]


