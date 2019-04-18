class NotNodeException(Exception):

    def __init__(self, klass, message=None, *args, **kwargs):
        if message is None:
            message = f"{klass} is not a subclass of BaseNode"
        return super().__init__(message, *args, **kwargs)
