# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 10:36:57 2021

@author: nandini.ananthan
"""

arr = [4, 5, 2, 10, 8]
OP = [-1, 4, -1, 2, 2]

#############     Using stack    ##################
'''
stack, res = [], []

for i in range(len(arr)):
    if len(stack) == 0:
        res.append(-1)
    elif stack and arr[i] > stack[-1]:
        res.append(stack[-1])
    elif stack and arr[i] < stack[-1]:
        while stack and arr[i] < stack[-1]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])
    stack.append(arr[i])

    print(res)
'''

            

            
            



