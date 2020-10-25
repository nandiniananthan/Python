# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 01:24:15 2020

@author: nandini.ananthan
"""

nums = [3,2,1]
op = 1

def thirdMax(nums):
    nums=set(nums)
    
    if len(nums) < 3:
        return max(nums)
    
    else:
        max_val = max(nums)
        nums.remove(max_val)
        max_val = max(nums)
        nums.remove(max_val)
        return max(nums)
        
                
print(thirdMax(nums))