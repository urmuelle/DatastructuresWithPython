#!/usr/bin/python

class myClass:
    def __init__(self, classi, name):
        self.name = name
        self.classi = classi

    def classFunction(self, variable):
        test = variable + 500
        print(test)    


def myFunction(variable):
    test = variable + 5
    print(test)

n = input('Zahl eingeben: ')

i = 5

print('Hallo Welt\n', i)
print('Noch mehr Welt', n)
myFunction(3.5)
instance = myClass(10, 'Hallo')
instance.classFunction(3.5)
print(instance.classi)
