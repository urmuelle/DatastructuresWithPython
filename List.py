"""
Program to implement datastructures 
- "Linked List" 
- "Cyclic Linked List"
in python 3
"""

# Class representing a linked list node
class Node:
    def __init__(self, value=None, next=None):
        self.value = value
        self.next = next

# Class representing a single linked list
class LinkedList:
    """
    Linked list with help - nodes head (marks start of the list)
    and node z (marks end of the list)
    """
    def __init__(self):
        self.count = 0
        self.head = Node()
        self.z = Node()
        self.head.next = self.z

    def deleteNext(self, node):
        node.next = node.next.next
        
    def insertAfter(self, value, node):
        x = Node(value, node.next)
        node.next = x
        return x

    def printList(self):
        n = self.head.next
        while (n != self.z):
            print(n.value)
            n = n.next

class CyclicLinkedList:
    """
    Linked list with help - node head (marks start of the list)    
    """
    def __init__(self):
        self.count = 0
        self.head = None

    def deleteNext(self, node):
        node.next = node.next.next
        
    def insertAfter(self, value, node):
        x = Node(value)
        if (self.head == None):
            x.next = x
            self.head = x
        else:
            x.next = node.next
            node.next = x
        return x

    def insertLast(self, value):
        if (self.head == None):
            x = Node(value)
            self.head = x
            x.next = x
            return x
        else:
            x = self.head
            while (x.next != self.head):
                x = x.next
            return self.insertAfter(value, x)

    def printList(self):        
        print(self.head.value)
        n = self.head.next
        while (n != self.head):
            print(n.value)
            n = n.next

# Do tests on the new LinkedList class
l = LinkedList()
n1 = l.insertAfter(1, l.head)
n2 = l.insertAfter(2, n1)
print('printing list')
l.printList()

# Josephus Problem - who is last man standing
m = 5
n = 9
l = CyclicLinkedList()
for i in range(1, n+1):
    rn = l.insertLast(i)
print('printing Josephus List')
l.printList()

# remove every mth item until last item remains
n = rn
while (n != n.next):
    for i in range(0, m-1):
        n = n.next
    print('deleting node: ', n.next.value)
    l.deleteNext(n)
print('Last man standing: ', n.value)
