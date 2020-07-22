# -*- coding: utf-8 -*-
"""
Created on Wed Jul 22 09:55:39 2020

@author: nandini.ananthan
"""

############        Solution 1          #############

nums = [0,0,1]
OP = [1,0,0]
j = 0

for i in range(len(nums)):
    if nums[i] != 0:
        nums[i], nums[j] = nums[j], nums[i]
        j += 1
print(nums)

########      Solution 2 ###########

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """            
        for i in range(len(nums)):
            for j in range(len(nums)):
                if nums[j] == 0:
                    val = nums.pop(j)
                    nums.append(val)
        return (nums)
        