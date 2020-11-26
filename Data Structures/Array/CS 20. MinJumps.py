# -*- coding: utf-8 -*-
"""
Created on Wed Nov 25 15:22:29 2020

@author: nandini.ananthan
"""

inputArray = [1, 4, 10, 6, 2]
OP = 4

def avoidObstacles(a):
    i = 2
    while True:
        if all([n % i != 0 for n in a]):
            return i
        i += 1
        
print(avoidObstacles(inputArray))
