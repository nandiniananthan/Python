# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 16:20:13 2021

@author: nandini.ananthan
"""
arr = [100, 80, 60, 70, 60, 75, 85]
OP =  [1,   1,  1,  2,  1,  4,  6]

res = []
stack = []
res.append(1)

for i in range(len(arr)):
    if len(arr) == 0:
        res.append(1)
    elif stack and arr[i] < stack[-1][0]:
        index = stack[-1][1]
        val = i - index
        #res.append(stack[-1])
        res.append(val)
    elif stack and arr[i] > stack[-1][0]:
        while stack and arr[i] > stack[-1][0]:
            stack.pop()
        if not stack:
            res.append(1)
        else:
            index = stack[-1][1]
            val = i - index
            #res.append(stack[-1])
            res.append(val)
    stack.append((arr[i],i))

print(res)

    

    
