# -*- coding: utf-8 -*-
"""
Created on Tue Dec  1 11:23:55 2020

@author: nandini.ananthan
"""

q = [2, 3, 4, 1, 5]

count = 0

for i in range(len(q)):
    while q[i] != i+1:
        temp = q[i] - 1
        q[i], q[temp] = q[temp], q[i]
        print(q)
        count += 1

print(count)

