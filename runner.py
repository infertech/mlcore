from exceptions import NotNodeException
from nodes import BaseNode


def run(nodes, data):
    # Verify argument types
    for node in nodes:
        if not isinstance(node, BaseNode):
            raise NotNodeException(klass=node.__class__)
    # Start data processing
    for node in nodes:
        data = node.process(data)
    return data
