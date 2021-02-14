# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 20:01:52 2021

@author: nandini.ananthan
"""
import collections

s1 = "watertables"
s2 = "erbottlewat"

def isSubstring(s1, s2):
    if len(s1) != len(s2) or collections.Counter(s1.lower()) != collections.Counter(s2.lower()):
       return False
    return True

print(isSubstring(s1, s2))
