# -*- coding: utf-8 -*-
"""
Created on Wed Sep  2 18:55:04 2020

@author: nandini.ananthan
"""

n = "00000000000000000000000000001011"

class Solution:
    def hammingWeight(self, n: int) -> int:
        return bin(n).count('1')
        
