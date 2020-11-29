# -*- coding: utf-8 -*-
"""
Created on Sat Nov 28 13:00:33 2020

@author: nandini.ananthan
"""
n = 6
c = [0, 0, 0, 1, 0, 0]
OP = 3

def jumpingOnClouds(c):
    if len(c) == 2:
        return 1 if c[1] == 0 else 0
    count = 0
    i = 0
    while i < len(c)-2:
        if c[i+2] == 1:
            i += 1 
            count += 1
        else:
            i += 2
            count += 1
        if i == len(c)-2:
            count += 1
            
    return(count)


print(jumpingOnClouds(c))
