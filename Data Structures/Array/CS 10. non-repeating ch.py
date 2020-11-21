# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 20:35:06 2020

@author: nandini.ananthan
"""

s = "abacabaabacaba"
Op = 'c'

def firstNotRepeatingCharacter(s):
    n = len(s)
    dict1 = {}
    for i in range(n):
        if s[i] in dict1:
            dict1[s[i]] += 1
        else:
            dict1[s[i]] = 1
    for key, value in dict1.items():
        if 1 == value:
            return (key)
            break
    return "_"
