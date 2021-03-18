# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 15:47:17 2021

@author: nandini.ananthan
"""

arr = [4, 5, 2, 10, 8]
OP  = [2, 2, -1, 8, -1]

stack = []
res = []

for i in range(len(arr)-1, -1, -1):
    if len(arr) == 0:
        res.append(-1)
    elif stack and arr[i] > stack[-1]:
        res.append(stack[-1])
    elif stack and arr[i] <= stack[-1]:
        while stack and arr[i] <= stack[-1]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])
    stack.append(arr[i])
    
res = res[::-1]
res.append(-1)
print(res)    