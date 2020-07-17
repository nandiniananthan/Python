# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 13:05:02 2020

@author: nandini.ananthan
"""
nums = [1,2,3,1,1,3]
arr1 = []
for i in range(len(nums)):
    for j in range(len(nums)):
        if nums[i] == nums[j] and  i < j:
            arr1.append([i,j])
       # else:
        #    print("false")
print(arr1)   
print (len(arr1))

########     BEST SOLN     ########

nums = [1,2,3,1,1,3]
arr1 = 0
for i in range(len(nums)):
    for j in range(i):
        arr1 += nums[i]==nums[j]
print(arr1)
