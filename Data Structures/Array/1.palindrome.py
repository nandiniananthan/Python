# -*- coding: utf-8 -*-
"""
Created on Wed Nov 18 23:37:45 2020

@author: nandini.ananthan
"""

str1 = 'abas'

def palindrome(str1):
    return str1 == str1[::-1]

print(palindrome(str1))