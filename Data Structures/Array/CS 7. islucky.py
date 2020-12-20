# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:47:58 2020

@author: nandini.ananthan
"""

n = 1230

def isLucky(n):
    mid = len(str(n))//2
    sum1 = sum2 = 0
    n = str(n)
    
    for m in range(mid):
        sum1 += int(n[m])
    
    for m in range(mid,len(str(n))):
        sum2 += int(n[m])
    
    return sum1 == sum2