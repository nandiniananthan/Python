# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 12:18:29 2020

@author: nandini.ananthan
"""

n = 8
steps = 'UDDDUDUU'

def countingValleys(n, steps):
    seaLevel = valley = 0

    for step in steps:
        if step == 'U':
            seaLevel += 1
        else:
            seaLevel -= 1
        
        if step == 'U' and seaLevel == 0:
            valley += 1
    
    return valley

print(countingValleys(n, steps))
