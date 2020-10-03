# -*- coding: utf-8 -*-
"""
Created on Sat Oct  3 15:08:30 2020

@author: nandini.ananthan
"""
from collections import Counter

nums = [3,1,4,1,5]
k = 2

##########    using hashmap       #############

def findPairs(nums, k):
    result = 0
    dict1 = Counter(nums)
    for x in dict1:
        if k == 0 and dict1[x] >1:
            result += 1
        elif k > 0 and x+k in dict1:
            result += 1
    return result
    
print(findPairs(nums, k))


