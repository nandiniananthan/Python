# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 11:07:06 2020

@author: nandini.ananthan
"""

nums = [1,3,4,2,2]

#########   sorting and finding the adjacent duplicate value     ########
'''
def findDuplicate(nums):
    nums.sort()
    n = len(nums)
    for i in range(n):
        if nums[i] == nums[i-1]:
            return nums[i]
    return

##########   SET   ############
    
def findDuplicate(nums):
    nums1 = set()
    for num in nums:
        if num in nums1:
            return num
        nums1.add(num)
        
print(findDuplicate(nums))
'''
##########   DICTIONARY   ############

def findDuplicate(nums):
    dict1 = {}
    for num in nums:
        if num not in dict1:
            dict1[num] = 1
        else:
            return num
        
print(findDuplicate(nums))

