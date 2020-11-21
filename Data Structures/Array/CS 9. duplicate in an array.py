# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 11:21:26 2020

@author: nandini.ananthan
"""

a = [2, 1, 3, 5, 3, 2]
Op = 3

dict1 = {}
def firstDuplicate(a):
    for i in range(len(a)):
        if a[i] not in dict1:
            dict1[a[i]] = 1
        else:
            return a[i]

print(firstDuplicate(a))
