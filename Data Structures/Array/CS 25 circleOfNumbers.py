# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 10:00:01 2021

@author: nandini.ananthan
"""

cell1 = "B2"
cell2 = "C3"

def circleOfNumbers(n, firstNumber):
    ans = firstNumber + (n//2)
    if ans > n-1:
        ans = firstNumber - (n//2)
    return ans
    
