# -*- coding: utf-8 -*-
"""
Created on Tue Nov 17 15:58:22 2020

@author: nandini.ananthan
"""

arr = [2,3,2]
Output: False

def validMountainArray( A):
    N = len(A)
    i = 0

    # walk up
    while i+1 < N and A[i] < A[i+1]:
        i += 1

    # peak can't be first or last
    if i == 0 or i == N-1:
        return False

    # walk down
    while i+1 < N and A[i] > A[i+1]:
        i += 1

    return i == N-1
print(validMountainArray(arr))
        
