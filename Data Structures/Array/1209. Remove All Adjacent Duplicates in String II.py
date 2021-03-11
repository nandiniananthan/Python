# -*- coding: utf-8 -*-
"""
Created on Thu Mar 11 11:52:31 2021

@author: nandini.ananthan
"""

Input: s = "abcd"
k = 2
Output: "abcd"


class Solution:
    def removeDuplicates(self, S: str, k: int) -> str:
        distinct = set(S)
        toRemove = list()
        for char in distinct:
            toRemove.append(char*k)
            
        while True:
            start = S
            print(S)
            for dup in toRemove:
                if dup in S:
                    S = S.replace(dup, "")
                    #print(S)
            if start == S:
                return S
                
                