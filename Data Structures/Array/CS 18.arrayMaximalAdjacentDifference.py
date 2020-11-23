# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:46:06 2020

@author: nandini.ananthan
"""

inputArray = [10, 11, 13]

def arrayMaximalAdjacentDifference(inputArray):
    arr1 = []
    n = len(inputArray)
    for i in range(1,n):
        arr1.append(abs(inputArray[i]-inputArray[i-1]))
    return (arr1)

print(arrayMaximalAdjacentDifference(inputArray))
