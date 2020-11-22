# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 23:06:25 2020

@author: nandini.ananthan
"""

a = [1, 2, 2]
b = [2, 1, 1]
OP = True

def areSimilar(a, b):
    m = len(a)
    n = len(b)
    count = 0
    
    if m != n:
        return False
    
    for i in range(m):
        if a[i] != b[i]:
            count += 1
    
    return count <= 2 and sorted(a) == sorted(b)

print(areSimilar(a, b))