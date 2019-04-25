class BaseNode:

    def process(self, data):
        raise NotImplementedError(
            "Nodes should redefine their 'proceeess' method")
