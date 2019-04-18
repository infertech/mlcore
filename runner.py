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


if __name__ == '__main__':
    import sys
    number = int(sys.argv[1])
    nodes = [BaseNode() for _ in range(number)]
    result = run(nodes, sys.argv[2])
    print(result)
