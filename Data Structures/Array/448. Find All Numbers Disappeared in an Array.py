# -*- coding: utf-8 -*-
"""
Created on Tue Oct  6 18:18:47 2020

@author: nandini.ananthan
"""
'''
##########    using counter         ########
from collections import Counter

nums = [4,3,2,7,8,2,3,1]
Op = [5,6]
n = len(nums)

dict1 =(Counter(nums))
print(dict1)
arr1 = []

for i in range(1,(n)+1):
    if i not in dict1.keys():
        arr1.append(i)
    
print(arr1)
'''
##########    using hashmap         ########

nums = [4,3,2,7,8,2,3,1]
Op = [5,6]
n = len(nums)
dict1= {}
arr1 = []
for num in nums:
    dict1[num] = 1

for num in range(1,n+1):
    if num not in dict1:
        arr1.append(num)
print(arr1)