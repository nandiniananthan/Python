# -*- coding: utf-8 -*-
"""
Created on Wed Mar 17 21:06:17 2021

@author: nandini.ananthan
"""

arr = [1, 3, 2, 4]
OP =   [3, 4, 1, 1, 2, 4, -1]

############     Brute force    #########
'''
res = []

for i in range(len(arr1)):
    for j in range(i, len(arr1)):
        if arr1[j] > arr1[i]:
            res.append(arr1[j])
            break

res.append(-1)
print(res)
'''

##########   using stack     ##########
arr = [1, 3, 0, 0, 1, 2, 4]
OP =  [3, 4, 1, 1, 2, 4, -1]
stack = []
res = []

for i in range(len(arr)-1, -1, -1):
    if len(arr) == 0:
        res.append(-1)
        #print(res)
    elif len(stack) > 0 and stack[-1] > arr[i]:
        res.append(stack[-1])
    elif len(stack) > 0 and arr[i] >= stack[-1]:
        while len(stack) > 0 and arr[i] >= stack[-1]:  
            stack.pop()
        if len(stack) == 0:
            res.append(-1)
        elif arr[i] <= stack[-1]:
            res.append(stack[-1])
    stack.append(arr[i])

res = res[::-1]
res.append(-1)
print(res)    

        
        
        
        
        
        
        
        
        
    