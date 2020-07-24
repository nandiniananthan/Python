# -*- coding: utf-8 -*-
"""
Created on Thu Jul 23 17:03:31 2020

@author: nandini.ananthan
"""


a = -2
b = 3
arr1 = []
arr1.append(a)
arr1.append(b)
sum = 0


for i in range(len(arr1)):
    sum += arr1[i]
print(sum)