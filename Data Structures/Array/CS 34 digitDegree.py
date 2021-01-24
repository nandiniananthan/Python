# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:37:45 2021

@author: nandini.ananthan
"""

n = 92

def find_sum(n):
    ans = 0
    for i in str(n):
        ans += int(i)
    return ans

count = 0

while n > 9:
    n = sum(int(i) for i in str(n))
    print(n)
    count += 1

print(count)


