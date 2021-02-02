# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:16:56 2021

@author: nandini.ananthan
"""

s1 = "wazup bro"
s2 = " orbpuwaz"

def similar(s1, s2):
    dict1 = {}
    
    for i in range(len(s1)):
        if s1[i] not in dict1:
            dict1[s1[i]] = 1
        else:
            dict1[s1[i]] += 1
    
    print(dict1)
    
    for i in range(len(s2)):
        if s2[i] not in dict1:
            return False
    return True

def similar1(s1, s2):
    if len(s1) != len(s2):
        return False
    return sorted(s1) == sorted(s2)


print(similar1(s1, s2))

