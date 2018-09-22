"""
Program to implement datastructure
- "Queue" 
in Python 3
"""

# Class representing a Queue
class PythonQueue:
    """
    Queue implemented on the basis of a linked list with help - nodes head
    (marks start of the list) and node z (marks end of the list)
    """
    def __init__(self):
        self.items = []

    def put(self, value):
        self.items.append(value)

    def get(self):
        t = self.items.pop(0)
        return t

    def empty(self):
        return self.items.count == 0

    def printQueue(self):        
        print(self.items)

# Test queue functions
q = PythonQueue()

q.put('A')
print(q.get())
q.printQueue()
q.put('S')
q.put('A')
print(q.get())
q.printQueue()
q.put('M')
print(q.get())
q.printQueue()
q.put('P')
print(q.get())
q.printQueue()
q.put('L')
q.put('E')
print(q.get())
q.printQueue()
q.put('Q')
print(q.get())
q.printQueue()
print(q.get())
q.printQueue()
print(q.get())
q.printQueue()
q.put('U')
print(q.get())
q.printQueue()
q.put('E')
q.put('U')
print(q.get())
q.printQueue()
q.put('E')
print(q.get())
q.printQueue()
