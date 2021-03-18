# -*- coding: utf-8 -*-
"""
Created on Thu Mar 18 00:54:53 2021

@author: nandini.ananthan
"""

arr = [1, 3, 2, 4]
OP =  [-1, -1, 3, -1]

stack = []
res = []

for i in range(len(arr)):
    if len(stack) == 0:
        res.append(-1)
    elif len(stack) > 0 and arr[i] < stack[-1]:
        res.append(stack[-1])
    elif len(stack) > 0 and arr[i] >= stack[-1]:
        while len(stack) > 0 and arr[i] >= stack[-1]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1])
    stack.append(arr[i])
    #print("res is",res)
    #print("stack is", stack)
    #print("")
    
    
#res = res[::-1]
print(res)



 
