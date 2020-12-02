# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:54:13 2020

@author: nandini.ananthan
"""

int_list = [1, 7, 3, 4]
OP =   [84, 12, 28, 21]


n = len(int_list)
left = [1] * len(int_list)
right = [1] * len(int_list)
res = [1] * len(int_list)

for i in range(1,n):
    left[i] = left[i-1] * int_list[i-1]

for i in range(n-2,-1,-1):
    right[i] = right[i+1] * int_list[i+1]
    
for i in range(n):
    res[i] = left[i] * right[i]

print(res)    
        