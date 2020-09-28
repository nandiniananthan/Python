# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 13:32:20 2020

@author: nandini.ananthan
"""

x = 18

def mySqrt(x):
     l = 0
     h = x
     if x < 2:
         return x
     while l <= h:
         mid = (l + h) // 2
         print(mid)
         if mid*mid <= x < (mid+1)*(mid+1):
             print("squareis",mid*mid)
             return mid
         elif x  < mid*mid:
             h = mid
         else:
             l = mid
             
print("ans is",mySqrt(x))

