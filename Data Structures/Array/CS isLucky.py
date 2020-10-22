# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 17:14:27 2020

@author: nandini.ananthan
"""

n = 1230
op= True

def isLucky(n):
    s = [int(x) for x in str(n)]
    l = int(len(s)/2)
    return sum(s[:l]) == sum(s[l:])

print(isLucky(n))
