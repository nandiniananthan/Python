# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 19:09:35 2020

@author: nandini.ananthan
"""
from collections import Counter
arr = [2,2]
# Missing = 2, Repeating = 3
dict1 = Counter(arr)
missing, repeating = 0,0

for i in range(1,len(arr)+1):
    if i not in dict1.keys():
        missing = i
    
for k,v in dict1.items():
    if v > 1:
        repeating = k



print(repeating, missing)
        

