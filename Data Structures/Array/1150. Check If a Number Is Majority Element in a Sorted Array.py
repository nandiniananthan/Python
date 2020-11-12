# -*- coding: utf-8 -*-
"""
Created on Wed Nov 11 20:20:08 2020

@author: nandini.ananthan
"""

nums = [10,100,101,101]
target = 101
Output = True

'''
############        dict         ############
def isMajorityElement(nums,target):
    dict1 = {}
    
    for i in range(len(nums)):
        if nums[i] in dict1:
            dict1[nums[i]] += 1
        else:
            dict1[nums[i]] = 1
        
    for key,val in dict1.items():
        key = max(dict1, key=dict1.get)
        if val > len(nums)//2 and key == target:
            return True
    return False


def isMajorityElement(nums,target):
    n = len(nums)
    count = 0
    
    for num in nums:
        if num == target: 
            count += 1
    return count > n//2

'''
def isMajorityElement(nums,target):
    return nums.count(target) > len(nums)//2     
    
    
print(isMajorityElement(nums, target))