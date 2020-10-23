# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 10:41:27 2020

@author: nandini.ananthan
"""

s = "abcdabcbb"
Output: 3

start = 0
n = len(s)
dict1 = {}
ans = 0

for i in range(n):
    if s[i] in dict1 and start<=dict1[s[i]]:
        start = dict1[s[i]] + 1
    else:
        ans = max(ans, i-start+1)
    dict1[s[i]] = i

print(ans)
    

