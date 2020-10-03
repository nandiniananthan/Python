# -*- coding: utf-8 -*-
"""
Created on Fri Oct  2 16:14:11 2020

@author: nandini.ananthan
"""

nums = [1,3,5,6]
target = 7

def searchInsert(nums,target):
    low = 0
    high= len(nums)-1
    
    while low <= high:
        mid = (low+high)//2
        if target == nums[mid]:
            return mid
        if target < nums[mid]:
            high = mid-1
        else:
            low = mid+1
    return low
            
            
print(searchInsert(nums, target))   
         