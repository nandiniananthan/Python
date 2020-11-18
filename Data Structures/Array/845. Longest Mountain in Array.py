# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 17:28:21 2020

@author: nandini.ananthan
"""

arr = [0,1,2,3,4,5,4,3,2,1,0]
Output: 5

n = len(arr)
res= 0

for i in range(1,n-1):
    if arr[i-1] < arr[i] > arr[i+1]:
        l = r = i
    
        while l > 0 and arr[l-1] < arr[l]:
            l -= 1
            
        while r+1 < n and arr[r] > arr[r+1]:
            r += 1
        
        res = max(res, (r-l+1))

print(res)
