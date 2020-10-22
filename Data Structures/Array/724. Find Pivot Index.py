# -*- coding: utf-8 -*-
"""
Created on Wed Oct 21 21:50:01 2020

@author: nandini.ananthan
"""

nums = [1,2,3]
Output: 3

n = len(nums)
def pivotIndex(nums):
    leftsum = 0
    S = sum(nums)
    for idx,val in enumerate(nums):
        if leftsum == (S-leftsum-val):
            return idx
        leftsum += val
    return -1

print(pivotIndex(nums))
