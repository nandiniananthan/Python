# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 19:31:15 2021

@author: nandini.ananthan
"""

str1 = "passles"
str2 = "passlqq"

dict1 = {}

def palper(str1, str2):
    if abs(len(str1) - len(str2)) > 1:
        return False
    str1 = str1.lower()
    str1 = str1.replace(" ","")
    dict1 = {}
    
    for i in range(len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]] = 1
        else:
            dict1[str1[i]] += 1
    
    count = 0
    for j in range(len(str2)):
        if str2[j] not in dict1:
            count += 1
    
    if count > 1:
        return False
    return True

print(palper(str1, str2))