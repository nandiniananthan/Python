# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 09:37:57 2021

@author: nandini.ananthan
"""

nums1 = [4,1,2]
nums2 = [1,3,4,2]
Output = [-1,3,-1]


class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack = []
        result = []
        stack.append(nums2[0])
        dict1 = {}
        
        for i in range(1, len(nums2)):
            while stack and nums2[i] > stack[-1]:
                dict1[stack[-1]] = nums2[i]
                stack.pop()    
            stack.append(nums2[i])
        
        for element in stack:
            dict1[element] = -1
        
        for num in nums1:
            result.append(dict1[num])
        
        return result
            
            
            
        
        
                
            
            
        