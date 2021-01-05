# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:31:00 2021

@author: nandini.ananthan
"""

a = [2, 3]

def absoluteValuesSumMinimization(a):
    d = {}
    for c in a:
        ans = 0
        for b in a:
            ans += abs(b-c)
        d[c] = ans
    return (min(d, key=d.get))

