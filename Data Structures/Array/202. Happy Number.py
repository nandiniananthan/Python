# -*- coding: utf-8 -*-
"""
Created on Fri Sep  4 19:05:51 2020

@author: nandini.ananthan
"""

n = 19

def isHappy(n):
    temp = 0
    def ss(n):
        n = ' '.join(str(n)).split()
        temp = 0
        for m in n:
            temp += int(m) ** 2
        return temp
    
    seen = set()
    while ss(n) not in seen:
        temp = ss(n)
        if temp == 1:
            return True
        else:
            seen.add(temp)
            n = temp
    return False

print(isHappy(n))
