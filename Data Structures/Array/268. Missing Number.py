# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 20:01:43 2020

@author: nandini.ananthan
"""

nums = [9,6,4,2,3,5,7,0,1]
"""
#######    Brute force approach   ######

nums.sort()

if nums[0] != 0:
    print(0)

elif nums[-1] != len(nums):
    print(len(nums))
    
for i in range(len(nums)-1):
    if nums[i]+1 == nums[i+1]:
        pass
    
    else:
        print(nums[i]+1)
        
######  brute force 2   #######

class Solution:
    def missingNumber(self, nums):
        nums.sort()
        for i in range(len(nums)):
            if nums[i] != i:
                return i
        return len(nums)
"""  
######     HASH map     ########
        
nums_set = set(nums)
for num in range(len(nums)):
    if num not in nums_set:
        print(num)