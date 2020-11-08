# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:49:30 2020

@author: nandini.ananthan
"""

nums = [1,-1,0]
k = 0

Output = 3

def subarraySum(nums,k):
    count = 0
    s = 0
    d = {}
    d[0] = 1
    
    for i in range(len(nums)):
        s += nums[i]
        if s-k in d:
            count += d[s-k]
        if s in d:
            d[s] += 1
        else:
            d[s] = 1
    
    return count


print(subarraySum(nums, k))
