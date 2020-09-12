# -*- coding: utf-8 -*-
"""
Created on Sat Sep 12 11:09:33 2020

@author: nandini.ananthan
"""
import collections

s = "aaba"

def canPermutePalindrome(s):
    """
    :type s: str
    :rtype: bool
    """
    counter = collections.Counter(s)
    
    odd = 0
    
    for count in counter.values():
        if count % 2 != 0:
            odd += 1
        
        if odd > 1:
            return False
    
    return True

print(canPermutePalindrome(s))
