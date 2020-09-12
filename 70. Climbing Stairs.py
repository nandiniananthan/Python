# -*- coding: utf-8 -*-
"""
Created on Fri Sep 11 18:43:06 2020

@author: nandini.ananthan
"""

Input = 2,Output = 2

def climbStairs(n):
    if n == 0:
        return 0
    if n == 1:
        return 1
    if n == 2:
        return 2
    
    d = {1:1, 2:2}
    
    for i in range(3,n+1):
        curr = climbStairs[i-1] + climbStairs[i-2]
        d[i] = curr
    return d[n]

print(climbStairs(5))
