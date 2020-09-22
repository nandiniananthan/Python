# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:42:55 2020

@author: nandini.ananthan
"""
from collections import Counter

s = "anagram"
t = "nagaram"

'''
#########   sorting the strings    #######

def isAnagram(s,t):
    if len(set(s)) != len(set(t)):
        return False
    
    
    s = sorted(s)
    t = sorted(t)
    
    if s == t:
        return True
    return False
'''          
#########    using dictionary      #####
    
def isAnagram(s,t):
    d1 = {}
    d2 = {}
    for i in s:
        if i not in d1:
            d1[i] = 0
        d1[i] += 1
    for i in t:
        if i not in d2:
            d2[i] = 0
        d2[i] += 1
    return d1 == d2

print(isAnagram(s,t))
