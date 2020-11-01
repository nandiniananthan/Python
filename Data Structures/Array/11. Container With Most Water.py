# -*- coding: utf-8 -*-
"""
Created on Sat Oct 31 17:26:24 2020

@author: nandini.ananthan
"""

height = [1,8,6,2,5,4,8,3,7]
Output: 49

L, R = 0, len(height) - 1
res = 0
width = len(height) - 1

for w in range(width,0,-1):
    if height[L] < height[R]:
        res, L = max(res, height[L]*w), L+1
    else:
        res, R = max(res, height[R]*w), R-1
    
print(res)