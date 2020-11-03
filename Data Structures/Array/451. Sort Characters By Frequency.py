# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 19:34:20 2020

@author: nandini.ananthan
"""
from collections import Counter

Input = "tree"
Output = "eert"

c = Counter(Input)
arr1 = []

for key,val in c.most_common():
    arr1.append(key*val)
print(''.join(arr1))