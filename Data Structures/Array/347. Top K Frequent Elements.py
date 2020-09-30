# -*- coding: utf-8 -*-
"""
Created on Wed Sep 30 14:04:36 2020

@author: nandini.ananthan
"""

nums = [1,1,1,2,2,3]
k = 2
Output = [1,2]

from collections import Counter
import heapq

def topKFrequent(nums,k):
    dict1 = Counter(nums)
    return heapq.nlargest(k, dict1.keys(), key = dict1.get)

print(topKFrequent(nums, k))