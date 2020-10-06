# -*- coding: utf-8 -*-
"""
Created on Mon Oct  5 17:26:46 2020

@author: nandini.ananthan
"""

nums = [2,0,2,1,1,0]

Output = [0,0,1,1,2,2]

low = mid = 0
n = len(nums)
high = n-1

while mid<=high:
    if nums[mid] == 0:
        nums[low], nums[mid] = nums[mid], nums[low]
        low += 1
        mid += 1
        
    elif nums[mid] ==1:
        mid += 1
        
    else:
        nums[high], nums[mid] = nums[mid], nums[high]
        high -= 1

print(nums)