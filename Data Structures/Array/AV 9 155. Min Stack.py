# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 15:45:50 2021

@author: nandini.ananthan
"""

arr = [18, 19, 29, 15, 16]

class MinStack:

    def __init__(self):
        """
        initialize your data structure here.
        """
        self.stack = []
        self.ss = []

    def push(self, val: int) -> None:
        self.stack.append(val)
        if not self.ss or val <= self.ss[-1]:
            self.ss.append(val)        

    def pop(self) -> None:
        if self.ss[-1] == self.stack[-1]:
            self.ss.pop()
        self.stack.pop()

    def top(self) -> int:
        return self.stack[-1]
        

    def getMin(self) -> int:
        return self.ss[-1]
        


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(val)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()

