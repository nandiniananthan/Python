# -*- coding: utf-8 -*-
"""
Created on Tue Aug 25 19:35:41 2020

@author: nandini.ananthan
"""

nums = [-1, 0, 1, 2, -1, -4]
target = 0


    
def threeSum(nums):
    res = []
    nums.sort()
    for i in range(len(nums)):
        if nums[i] > 0:
            break
        if i == 0 or nums[i-1] != nums[i]:
            twosum(nums,i,res)
    return res

def twosum(nums,i,res):
    low, high = i+1, len(nums)-1
    while low < high:
        if nums[i] + nums[low] + nums[high] < 0:
            low += 1
        elif nums[i] + nums[low] + nums[high] > 0:
            high -= 1
        else:
            res.append([nums[i],nums[low],nums[high]])
            low += 1
            high -= 1
            while low < high and nums[low] == nums[low-1]:
                low+=1
                
print(threeSum(nums))        
