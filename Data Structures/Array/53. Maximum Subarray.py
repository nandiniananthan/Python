# -*- coding: utf-8 -*-
"""
Created on Sun Jul 19 01:21:55 2020

@author: nandini.ananthan
"""

nums = [-2,1,-3,4,-1,2,1,-5,4]

"""
current_sum = max_sum = nums[0]

for i in range(1,len(nums)):
    current_sum = max(nums[i], nums[i] + current_sum)
    max_sum = max(max_sum , current_sum)
print(max_sum)
"""

left_sum = right_sum = 0
class Solution:
    def individual_sum(self,nums,left,right):
        if left == right:
            return nums[left]
        
        p = (left+right) // 2
        
        left_sum = self.individual_sum(nums, left, p)
        right_sum = self.individual_sum(nums, p+1, right)
        cross_sum = self.cross_sum(nums, left, right, p)
        
        return max(left_sum, right_sum, cross_sum)
    
    def cross_sum(self,nums, left, right, p):
        if left == right:
            return nums[left]
        
        curr_sum = 0
        left_subsum = float('-inf')
        for i in range(p, left-1, -1):
            curr_sum += nums[i]
            left_subsum = max(left_subsum, curr_sum)
            
        curr_sum = 0
        right_subsum = float('-inf')
        for i in range(p+1, right + 1):
            curr_sum += nums[i]
            right_subsum = max(right_subsum, curr_sum)
        
        return left_subsum + right_subsum
    
    def maxSubArray(self, nums):
        return self.individual_sum(nums, 0, len(nums)-1)
        
        
        
        
    