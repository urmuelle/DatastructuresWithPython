"""
Program to implement Quicksort and its variants from chapter 9
in python 3
"""

from tkinter import *
from random import *
import time, _thread
import threading

# Class visualizing sorting
class SorterApp:
    def __init__(self, parent):
        self.myParent = parent
        self.canvas = Canvas(master=self.myParent, width=203, height=203, bg='white')
        self.canvas.pack(expand=YES, fill=BOTH)
        self.canvas.create_window(200, 200)
        self.button = Button(root)
        self.button.pack()
        self.values = list(range(100))
        self.myParent.after(10, self.update)        
        self._resetbutton()

    def _resetbutton(self):
        self.running = False
        self.button.config(text="Start", command=self.startthread)

    def startthread(self):
        self.running = True
        self.values = list(range(100))
        shuffle(self.values)
        newthread = threading.Thread(target=self.quicksort)
        newthread.start()
        self.button.config(text="Stop", command=self._resetbutton)

    def drawValues(self):
        self.canvas.delete('all')
        for i in range(100):
            self.canvas.create_rectangle(2*i, 200-2*self.values[i], 2*i+3, 200-2*self.values[i]+3, width=1, fill='black')

    def update(self):
        self.drawValues()
        self.myParent.after(10, self.update)    

    def quicksort(self):
        self.quickSortHelper(0, len(self.values) - 1)
        self._resetbutton()

    def quickSortHelper(self, first, last):
        if first < last:
            splitpoint = self.partition(first, last)

            self.quickSortHelper(first, splitpoint - 1)
            self.quickSortHelper(splitpoint + 1, last)

    def partition(self, first, last):
        pivotvalue = self.values[first]

        leftmark = first + 1
        rightmark = last

        done = False
        while not done:

            while leftmark <= rightmark and self.values[leftmark] <= pivotvalue:
                leftmark = leftmark + 1

            while self.values[rightmark] >= pivotvalue and rightmark >= leftmark:
                rightmark = rightmark - 1

            if rightmark < leftmark:
                done = True
            else:
                temp = self.values[leftmark]
                self.values[leftmark] = self.values[rightmark]
                self.values[rightmark] = temp

        time.sleep(0.01)
        temp = self.values[first]
        self.values[first] = self.values[rightmark]
        self.values[rightmark] = temp

        return rightmark


root = Tk()
app = SorterApp(root)
root.mainloop()
