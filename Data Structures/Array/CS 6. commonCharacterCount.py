# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 22:28:43 2020

@author: nandini.ananthan
"""
from collections import Counter
import operator

s1 = "aabcc"
s2 = "adcaa"

OP = 3

ans1 = Counter(s1) 
ans2 = Counter(s2)
ans = ans1 & ans2
ans = list(ans.elements())

print(len(''.join(ans)))


###############         new              ##############

res = 0
ans = set(s1) & set(s2)
for i in ans:
    res += min(s1.count(i),s2.count(i))
print(res)