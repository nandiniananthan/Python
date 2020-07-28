# -*- coding: utf-8 -*-
"""
Created on Tue Jul 21 23:04:46 2020

@author: nandini.ananthan
"""

nums = [1,2,3,4]
pdt = 1
arr1 = []

Output: [24,12,8,6]

for num in nums:
    pdt = pdt * num
    print(pdt)
    val = pdt // num
    print(val)
"""
    val = pdt // num
    arr1.append(val)
print(arr1)
"""