# -*- coding: utf-8 -*-
"""
Created on Thu Feb 25 15:10:30 2021

@author: nandini.ananthan
"""

T = [73, 74, 75, 71, 69, 72, 76, 73]
OP = [1, 1, 4, 2, 1, 1, 0, 0]

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        res = [0] * len(T)
        stack = [len(T) - 1]
        
        for i in range(len(T)-2, -1, -1):
            while stack and T[i] >= T[stack[-1]]:
                stack.pop()
            if stack:
                res[i] = (stack[-1] - i)
            else:
                res[i] = 0
            stack.append(i)
        return res 
    
              
                
        
            