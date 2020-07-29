# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 23:20:35 2020

@author: nandini.ananthan
"""
import collections

s = "leetcode"

count  = collections.Counter(s)

for idx,char in enumerate(s):
    if count[char] == 1:
        print(idx)

    
        
