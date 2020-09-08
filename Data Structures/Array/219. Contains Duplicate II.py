# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 12:23:47 2020

@author: nandini.ananthan
"""

nums = [1,2,3,1,2,3]
k = 2

def containsNearbyDuplicate(nums):
    dict = {}
    n = len(nums)
    for i in range(n):
        if nums[i] in dict:
            if (i - dict[nums[i]] <= k):
                return True
            else:
                dict[nums[i]] = i
        if nums[i] not in dict:
            dict[nums[i]] = i
    return False

print(containsNearbyDuplicate(nums))