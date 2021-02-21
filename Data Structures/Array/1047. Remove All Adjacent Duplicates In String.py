# -*- coding: utf-8 -*-
"""
Created on Sun Feb 21 11:19:21 2021

@author: nandini.ananthan
"""

Input: "abbaca"
Output: "ca"

class Solution:
    def removeDuplicates(self, S: str) -> str:
        stack = []
        for char in S:
            if stack and char == stack[-1]:
                stack.pop()
            else:
                stack.append(char)
        return ''.join(stack)
    
            
        
