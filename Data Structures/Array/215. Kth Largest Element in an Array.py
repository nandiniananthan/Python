# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 13:29:30 2020

@author: nandini.ananthan
"""

nums = [3,2,1,5,6,4]
k = 2

def findKthLargest(nums):
    nums.sort()
    return nums[-k]
