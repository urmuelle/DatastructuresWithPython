"""
Program to implement datastructure
- "BinaryTree" 
in python 3
"""

# Class representing a binary tree node
class Node:
    def __init__(self, data=None):
        self.data = data
        self.left = None
        self.right = None

    def printTree(self):
        if self.left:
            self.left.printTree()
        print(self.data)
        if self.right:
            self.right.printTree()

class PythonStack:
    """
    Stack implemented on the basis of built in list type
    """
    def __init__(self):
        self.count = 0
        self.items = []

    def push(self, value):
        self.items.append(value)
        self.count += 1

    def pop(self):
        self.count -= 1
        if self.count < 0:
            self.count = 0
        return self.items.pop()

    def empty(self):
        return len(self.items) == 0

    def printStack(self):        
        print(self.items)

# Method to tokenize a simple string consisting of basic 
# arithmetic operations and digits

def tokenize (string):
    token = ''
    tokens = []
    for char in string:
        if char in '()+*':
            #previous was a n-digit token - add it to the list of tokens
            if token:
                tokens.append(token)
                token = ''
            tokens.append(char)
        if char.isdigit():
            token += char
    return tokens


mstr = '(5*(((9+8)*(4*6))+70))'
print('converting string ' + mstr +':')

def infixToPostfix(tokenlist):
    reverseTokenlist = []
    for token in tokenlist:    
        if token == ')':
            reverseTokenlist.append(s.pop())
        if token == '+':
            s.push(token)
        if token == '*':
            s.push(token)
        if token.isdigit():
            reverseTokenlist.append(token)
    return reverseTokenlist

print('Calculation example:')

x = Node()
z = Node()

z.left = z
z.right = z

root = Node(10)
root.printTree()

s = PythonStack()
tokenlist = tokenize(mstr)
reverseTokenlist = infixToPostfix(tokenlist)

for token in reverseTokenlist:
    x = Node(token)
    if (token == '+') or (token == '*'):
        x.right = s.pop()
        x.left = s.pop()
    s.push(x)

s.printStack()
root = s.pop()
root.printTree()
