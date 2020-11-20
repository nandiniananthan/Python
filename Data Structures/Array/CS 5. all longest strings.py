# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 21:22:51 2020

@author: nandini.ananthan
"""

inputArray = ["abc",  "eeee",  "abcd",  "dcd"]

allLongestStrings = ["eeee",  "abcd"]

max_len = -1
arr1 = []

max_len = max(len(ele) for ele in inputArray)

arr1 = [ele for ele in inputArray if len(ele) == max_len]
        
print(arr1)
