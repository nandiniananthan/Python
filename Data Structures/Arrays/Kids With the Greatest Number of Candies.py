# -*- coding: utf-8 -*-
"""
Created on Sun Jul 12 20:08:29 2020

@author: nandini.ananthan
"""
class Solution:
    def kidsWithCandies(self, candies: List[int], extraCandies: int) -> List[bool]:
        arr1 = []
        for i in candies:
            if i+extraCandies >= max(candies):
                arr1.append(True)
            else:
                arr1.append(False)
        return arr1