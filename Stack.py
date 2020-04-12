class Stack:
    def __init__(self):
        self.structure = []

    def push(self, value):
        self.structure.append(value)

    def peek(self):
        toReturn=self.structure.pop()
        self.structure.append(toReturn)
        return toReturn

    def pop(self):
        return self.structure.pop()

    def isEmpty(slef):
        return len(self.structure) == 0
    
    def top(self):
        return len(self.structure)

    def passStackToArray(self):
        return self.structure