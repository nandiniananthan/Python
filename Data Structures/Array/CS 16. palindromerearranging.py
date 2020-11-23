# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:14:07 2020

@author: nandini.ananthan
"""
from collections import Counter

inputString = "aaaaaaaaaaaaaaaaaaaaaaaaaaaaaabc"

def palindromeRearranging(inputString):
    str1 = Counter(inputString)
    print(str1)
    count = 0
    
    for ele in str1:
        print(ele, str1[ele])
        if str1[ele] % 2 == 0:
            pass
        else:
            count += 1
        
    return count <= 1       

print(palindromeRearranging(inputString))
