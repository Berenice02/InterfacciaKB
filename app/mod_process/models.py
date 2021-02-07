class Task:
    def __init__(self, name, collaboration_type, functions):
        self.name = name
        self.collaboration_type = collaboration_type
        self.functions = functions

class Function:
    def __init__(self, id, type, pos, pos1, assigned_to):
        self.id = id
        self.type = type
        self.pos = pos
        self.pos1 = pos1
        self.assigned_to = assigned_to
        

class Constraint:
    def __init__(self, id, t1, t2):
        self.id = id
        self.t1 = t1
        self.t2 = t2