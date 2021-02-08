class Resource:
    def __init__(self, name, capacity):
        self.name = name
        self.capacity = capacity

class AggregateResource:
    def __init__(self, name, resources):
        self.name = name
        self.resources = resources