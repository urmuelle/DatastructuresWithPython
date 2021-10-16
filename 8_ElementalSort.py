"""
Program to implement sorting algorithms from chapter 8
- "Selection Sort" 
- "Insertion Sort"
- "Bubble Sort"
- "Shellsort"
No example is being provided for "Distribution Counting"
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
        newthread = threading.Thread(target=self.insertionSort)
        newthread.start()
        self.button.config(text="Stop", command=self._resetbutton)

    def drawValues(self):
        self.canvas.delete('all')
        for i in range(100):
            self.canvas.create_rectangle(2*i, 200-2*self.values[i], 2*i+3, 200-2*self.values[i]+3, width=1, fill='black')

    def update(self):
        self.drawValues()
        self.myParent.after(10, self.update)

    def selectionSort(self):
        N = len(self.values)
        for i in range(N):
            min = i
            for j in range (i+1, N):
                if self.values[j] < self.values[min]:
                    min = j
            t = self.values[min]
            self.values[min] = self.values[i]
            self.values[i] = t            
            time.sleep(0.01)
        self._resetbutton()

    def bubbleSort(self):
        N = len(self.values)
        for i in reversed(range(1, N+1)):
            for j in range (1, i):
                if self.values[j-1] > self.values[j]:
                    t = self.values[j-1]
                    self.values[j-1] = self.values[j]
                    self.values[j] = t
                    time.sleep(0.005)
        self._resetbutton()

    def insertionSort(self):
        N = len(self.values)
        for i in range(1, N):
            v = self.values[i]
            j = i
            while ((self.values[j-1] > v) and (j > 0)):
                self.values[j] = self.values[j-1]
                time.sleep(0.005)
                j = j-1
            self.values[j] = v
        self._resetbutton()

    def shellSort(self):
        "Shell sort using Shell's (original) gap sequence: n/2, n/4, ..., 1."
        gap = len(self.values) // 2
        # loop over the gaps
        while gap > 0:
            # do the insertion sort
            for i in range(gap, len(self.values)):
                val = self.values[i]
                j = i
                while j >= gap and self.values[j - gap] > val:
                    self.values[j] = self.values[j - gap]
                    time.sleep(0.005)
                    j -= gap
                self.values[j] = val
            gap //= 2
        self._resetbutton()          

root = Tk()
app = SorterApp(root)
root.mainloop()
