# -*- coding: utf-8 -*-
"""
Created on Thu Oct  1 22:22:23 2020

@author: nandini.ananthan
"""

nums = [4,5,6,7,0,1,2]
target = 0

def search(nums, target):
    begin = 0
    end = len(nums) - 1 
    while begin <= end:
        mid = (begin + end)//2
        if nums[mid] == target:
            return mid
        if nums[mid] > nums[end]: # Left side of mid is sorted
            if  nums[begin] <= target and target < nums[mid]: # Target in the left side
                end = mid - 1
            else: # in right side
                begin = mid + 1
        else: # Right side is sorted
            if  nums[mid] < target and target <= nums[end]: # Target in the right side
                begin = mid + 1
            else: # in left side
                end = mid - 1
    return -1  

        
print(search(nums, target))