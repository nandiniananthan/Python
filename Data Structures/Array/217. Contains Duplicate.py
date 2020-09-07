# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 10:51:41 2020

@author: nandini.ananthan
"""

nums = [1,1,1,3,3,4,3,2,4,2]
nums.sort()
OP = True

def containsDuplicate(nums):
    return len(nums) != len(set(nums))
    
print(containsDuplicate(nums))
