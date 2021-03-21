# -*- coding: utf-8 -*-
"""
Created on Sun Mar 21 11:46:55 2021

@author: nandini.ananthan
"""
###########   NS  to the left   ###########

arr = [6, 2, 5, 4, 5, 1, 6]
OP =[-1, -1, 2, 2, 4, -1, 1]

stack, res = [], []

for i in range(len(arr)):
    if len(stack) == 0:
        res.append(-1)
    elif stack and arr[i] > stack[-1][0]:
        res.append(stack[-1][1])
    elif stack and arr[i] < stack[-1][0]:
        while stack and arr[i] < stack[-1][0]:
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        else:
            res.append(stack[-1][1])
    stack.append([arr[i],i])

print(" NS  to the left: ",res)

###########   NS  to the right   ###########

arr = [6, 2, 5, 4, 5, 1, 6]
OP = [2, 1, 4, 1, 1, -1, -1]

stack, res1 = [], []

for i in range(len(arr)-1, -1, -1):
    if len(stack) == 0:
        res1.append(len(arr))
    elif stack and arr[i] > stack[-1][0]:
        res1.append(stack[-1][1])
    elif stack and arr[i] < stack[-1][0]:
        while stack and arr[i] < stack[-1][0]:
            stack.pop()
        if len(stack) == 0:
            res1.append(len(arr))
        else:
            res1.append(stack[-1][1])
    stack.append([arr[i],i])

res1 = res1[::-1]
print("NS  to the right: ",res)

###########   final answer   ###########

ans = []

for i in range(len(res)):
    val = res1[i] - res[i] - 1
    ans.append(val)
    
print("final ans is ",ans)




