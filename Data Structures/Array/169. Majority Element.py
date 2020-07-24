# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:14:40 2020

@author: nandini.ananthan
"""

######    Brute force- time limit exceeded #######
class Solution:
    def majorityElement(self, nums):
        majority_count = len(nums)//2
        for num in nums:
            count = sum(1 for elem in nums if elem == num)
            if count > majority_count:
                return num

######           Hash MAp          #########
class Solution:
    def majorityElement(self, nums):
        counts = collections.Counter(nums)
        return max(counts.keys(), key=counts.get)
    
#########     Array sort and return the middle element    ########
nums = [2,2,1,1,1,2,2]
nums.sort()
print (nums[len(nums)//2])


############    Boyer-Moore Voting Algorithm    #######

nums = [2,2,1,1,1,2,2]
count = 0
candidate = None

for num in nums:
    if count == 0:
        candidate = num
    count += (1 if num == candidate else -1)
print(candidate)