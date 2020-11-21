# -*- coding: utf-8 -*-
"""
Created on Fri Nov 20 18:08:48 2020

@author: nandini.ananthan
"""

a = [-1, 150, 190, 170, -1, -1, 160, 180]
OP = [-1, 150, 160, 170, -1, -1, 180, 190]
c = []

for i in range(len(a)):
    if(a[i]==-1):
        c.append(i)

while -1 in a:
    a.remove(-1)

a.sort()

for ind in c:
    a.insert(ind,-1)
    
print(a)
