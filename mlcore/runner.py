from datetime import datetime

from .exceptions import NotNodeException
from .nodes import BaseNode


def run(nodes, data):
    # Verify argument types
    for name, node in nodes:
        if not isinstance(node, BaseNode):
            raise NotNodeException(klass=node.__class__)

    global_log = []
    # Start data processing
    time_before = datetime.now()
    for name, node in nodes:
        global_log.append((time_before, f"Started processing {name}"))
        # Process node and save its log
        data = node.process(data)
        global_log += node.log_list
        # Log execution time
        time_after = datetime.now()
        delta = time_after - time_before
        global_log.append(
            (time_after, f"Finished processing {name} in {delta}"))
        time_before = time_after

    return data, global_log
