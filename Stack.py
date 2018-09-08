"""
Program to implement datastructure
- "Stack" 
in python 3
"""

# Class representing a stack list node
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Class representing a stack
class Stack:
    """
    Stack implemented on the basis of a linked list with help - nodes head
    (marks start of the list) and node z (marks end of the list)
    """
    def __init__(self):
        self.count = 0
        self.head = Node()
        self.z = Node()
        self.head.next = self.z

    def push(self, value):
        t = Node(value)
        t.next = self.head.next
        self.head.next = t        

    def pop(self):
        t = self.head.next
        self.head.next = t.next
        return t.value

    def empty(self):
        return self.head.next == self.z

    def printStack(self):        
        n = self.head.next
        while (n != self.z):
            print(n.value)
            n = n.next

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

# Do test with the stack class
s = PythonStack()
print('printing Stack')
s.printStack()
s.push(1)
print('printing Stack')
s.printStack()

# Reverse Polish notation example:
# Calculate the result of 5*(((9+8)*(4*6))+7)
s = PythonStack()
s.push(5)
s.push(9)
s.push(8)
s.push(s.pop()+s.pop())
s.push(4)
s.push(6)
s.push(s.pop()*s.pop())
s.push(s.pop()*s.pop())
s.push(7)
s.push(s.pop()+s.pop())
s.push(s.pop()*s.pop())

print('printing result:')
s.printStack()

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

# Try infix to postfix representation

mstr = '(5*(((9+8)*(4*6))+70))'
print('converting string ' + mstr +':')
tokens = tokenize(mstr)
s = PythonStack()

for token in tokens:
    if token == ')':
        print(s.pop(), end='')        
    if token == '+':
        s.push(token)
    if token == '*':
        s.push(token)
    if token.isdigit():        
        print(token, end='')        
    if token != '(':
        print(' ', end='')

print('')
print('')

# Method to convert Infix to Postfix expressions

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

s = PythonStack()
tokenlist = tokenize(mstr)
reverseTokenlist = infixToPostfix(tokenlist)

for token in reverseTokenlist:
    x = 0
    if token == '+':
        x = int(s.pop()) + int(s.pop())
    if token == '*':
        x = int(s.pop()) * int(s.pop())
    if token.isnumeric():
        x = token
    s.push(x)

print(x)
