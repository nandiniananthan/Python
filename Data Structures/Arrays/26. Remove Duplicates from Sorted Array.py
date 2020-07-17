# -*- coding: utf-8 -*-
"""
Created on Fri Jul 17 12:34:00 2020

@author: nandini.ananthan
"""

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        j = 0
        n = len(nums)
        
        if n == 0 or n == 1:
            return nums

        for i in range(1,n):
            if nums[i] != nums[i-1]:
                nums[j] = nums[i]
                j += 1

        nums[j] = nums[-1]
        j += 1

        return (j)
    
    
class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        if not nums: return 0
        i, j = 0, 0
        while j < len(nums):
            if nums[i] != nums[j]:
                i += 1
                nums[i] = nums[j]
            j += 1
        return i + 1