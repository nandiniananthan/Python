# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

A = [34,23,1,24,75,33,54,8]
K = 60
Output: 58

############     Brute force       ###########
'''
def twoSumLessThanK(A,K):
    S = -1
    A.sort()
    for i in range(len(A)):
        for j in range(i+1, len(A)):
            if A[i] + A[j] < K:
                S = max(S, A[i]+A[j])
    return S

############      Two pointer        ############3
def twoSumLessThanK(A,K):
    low = 0
    high = len(A) - 1
    ans = -1
    A.sort()
    
    while low < high:
        if A[low] + A[high] < K:
            ans = max (ans, A[low] + A[high])
            low += 1
        else:
            high -= 1
    
    return (ans)
'''
    