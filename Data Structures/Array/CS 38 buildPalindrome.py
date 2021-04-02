# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 00:22:20 2021

@author: nandini.ananthan
"""

st = "abcdc"
OP = "abcdcba"

def buildPalindrome(st):
    for i in range(len(st)):
        subS = st[i:]
        if isPalindrome(subS):
            nonPal = st[0:i]
            return st + nonPal[::-1]

def isPalindrome(st):
    return st == st[::-1]
    
        
    
    
    
    


