# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 10:58:30 2020

@author: nandini.ananthan
"""

nums = [1,2,3,4]


def productExceptSelf(arr):
    left = [1]* len(nums)
        
    for i in range(1,len(nums)):
        left[i] = left[i-1] * nums[i-1]
        
    right = [1]* len(nums)
    for i in range(len(nums)-2,-1,-1):
        right[i] = right[i+1] * nums[i+1]
    
    res = [1]* len(nums)
    for i in range(len(nums)):
        res[i] = left[i] * right[i]
    
    return res
    
print(productExceptSelf(nums))