# -*- coding: utf-8 -*-
"""
Created on Wed Sep  9 19:45:40 2020

@author: nandini.ananthan
"""

#########################  using list   #
nums = [2,2,1]
nums.sort()
arr1 = []

def singleNumber(nums):
    for i in range(len(nums)):
        if nums[i] not in arr1:
            arr1.append(nums[i])
        else:
            arr1.remove(nums[i])
    return arr1.pop()
        
print(singleNumber(nums))


########################   using dictionary  #
nums = [4,1,2,1,2]

def unique(nums):
    dict = {}
    for num in nums:
        if num not in dict:
            dict[num] = 1
        else:
            dict[num] += 1
    
    for key,val in dict.items():
        if val == 1:
            return key
        
print(unique(nums))

#################   bit manipulation       #
nums = [4,1,2,1,2]

def unique(nums):
    res = 0
    for num in nums:
        res ^= num
    return res

print(unique(nums))
    
    
