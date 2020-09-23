# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 23:15:00 2020

@author: nandini.ananthan
"""

nums1 = [1,2,2,1]
nums1.sort()
nums1 = set(nums1)
nums2 = [2,2]
nums2.sort()
nums2 = set(nums2)

op = [2]

def intersection(nums1,nums2):
    nums1.sort()
    nums1 = set(nums1)
    nums2.sort()
    nums2 = set(nums2)
    dict1 = {}
    arr1 = []
    for num in nums1:
        if num not in dict1:
            dict1[num] = 1
        else:
            dict1[num] += 1
    
    for num in nums2:
        if num in dict1:
            arr1.append(num)
            
    return arr1

print(intersection(nums1,nums2))
