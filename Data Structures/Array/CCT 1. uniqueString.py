# -*- coding: utf-8 -*-
"""
Created on Tue Jan 26 17:02:30 2021

@author: nandini.ananthan
"""

from collections import Counter

str1 = "abcaa"

############     Brute Force solutions     ##########
'''
def unique(str1):
    for i in range(len(str1)):
        for j in range(i+1,len(str1)):
            if str1[i] == str1[j]:
                return False
    return True

'''

def unique1(str1):
    dict1 = {}
    for i in range(len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]] = 1
        else:
            return False
    return True
    
#print(unique1(str1))

def unique2(str1):
    s = sorted(str1)
    for i in range(len(s)):
        if s[i] == s[i-1]:
            return False
    return True

print(unique2(str1))


