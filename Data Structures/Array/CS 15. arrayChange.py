# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 14:55:53 2020

@author: nandini.ananthan
"""

inputArray = [2, 3, 3, 5, 5, 5, 4, 12, 12, 10, 15]

def arrayChange(inputArray):
    n = len(inputArray)
    count = 0
    r = 0

    for i in range(n-1):
        if inputArray[i+1] <= inputArray[i]:
            r=abs(inputArray[i]-inputArray[i+1])+1
            inputArray[i+1]=inputArray[i+1]+r
            count+=r
    return count