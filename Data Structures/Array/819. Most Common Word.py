# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 19:15:18 2020

@author: nandini.ananthan
"""
import collections 
import heapq

paragraph = "Bob hit a ball, the hit BALL flew far after it was hit."
banned = ["hit"]
Output = "ball"

normal_str = ''.join([c.lower() if c.isalnum() else ' ' for c in paragraph])

print(normal_str)
words = normal_str.split()
print(words)
dict1 = collections.Counter(words)
print(dict1)
arr1 = []
for key,val in dict1.items():
    if not key in banned:
        heapq.heappush(arr1, [-val,key])
print(heapq.heappop(arr1)[1])
