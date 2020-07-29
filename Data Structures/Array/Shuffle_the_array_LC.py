# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 13:12:30 2020

@author: nandini.ananthan
"""
nums = [2,5,1,3,4,7]
print("the array is",nums)
len1 = int(len(nums)/2)
print(len1)
n = 3
arr1 = []
"""
for i in range(len1):
    for n in range(len1,len(nums)):
        arr1.append(nums[i])
        arr1.append(nums[n])
        i += 1
        n += 1
    break
print(arr1)
"""
for i in range(len(nums)-n):
    arr1.append(nums[i])
    arr1.append(nums[i+n])
print(arr1)