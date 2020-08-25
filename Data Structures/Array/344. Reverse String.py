# -*- coding: utf-8 -*-
"""
Created on Mon Aug 24 13:32:11 2020

@author: nandini.ananthan
"""

s = ["h","e","l","l","o"]

left,right = 0,len(s)-1

while left < right:
    s[left], s[right] = s[right], s[left]
    left, right = left+1, right+1
print(s)