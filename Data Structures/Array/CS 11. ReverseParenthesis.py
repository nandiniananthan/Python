# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 20:35:18 2020

@author: nandini.ananthan
"""

inputString = "(bar)"
OP = "rab"

arr1 = []
char = list(inputString)

def rev(inputString):
    arr1 = []
    char = list(inputString)
    for i,v in enumerate(char):
        if v == '(':
            arr1.append(i)
        if v == ')':
            j = arr1.pop()
            char[j:i] = char[i:j:-1]
    return ''.join(c for c in char if c not in '()')

print(rev(inputString))
        