# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 16:24:54 2021

@author: nandini.ananthan
"""

str1 = "Tact Cpoa"
OP = True

def palper(str1):
    str1 = str1.lower()
    str1 = str1.replace(" ","")
    dict1 = {}
    
    for i in range(len(str1)):
        if str1[i] not in dict1:
            dict1[str1[i]] = 1
        else:
            dict1[str1[i]] += 1

    count = 0
    for k,v in dict1.items():
        print (k,v)
        if v == 1:
            count += 1
    
    return count == 1

print(palper(str1))

    

