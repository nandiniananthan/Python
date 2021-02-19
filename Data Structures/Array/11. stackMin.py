# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 21:39:45 2021

@author: nandini.ananthan
"""

class minStack:
    def __init__(self):
        self.items = []
    
    def push(self, item):
        if len(self.items) == 0:
            self.items.append((item, item))
        else:
            self.items.append((item, min(item, self.items[-1][1])))
            
    def pop(self):
        if len(self.items) > 0:
            return self.items.pop()[0]
    
    def min(self):
        if len(self.items) > 0:
            return self.items[-1][1]
            
            