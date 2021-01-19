# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 09:23:23 2021

@author: nandini.ananthan
"""

inputArray = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
k = 3
arr1 = []

def extractEachKth(inputArray, k):
    return [i for (n,i) in enumerate(inputArray) if (n+1) % k != 0]