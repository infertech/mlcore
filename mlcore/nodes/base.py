from datetime import datetime


class BaseNode:

    def __init__(self, params):
        self.params = params
        self.log_list = []

    def process(self, data):
        raise NotImplementedError(
            "Nodes should redefine their 'process' method")

    def log(self, data):
        """Log string representation of the data with timestamp"""
        string = str(data)
        timestamp = datetime.now()
        self.log_list.append((timestamp, string))
