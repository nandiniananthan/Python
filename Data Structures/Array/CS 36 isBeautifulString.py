# -*- coding: utf-8 -*-
"""
Created on Tue Mar 30 21:04:55 2021

@author: nandini.ananthan
"""
import string 

inputString = "bbbaaaa"

def isBeautifulString(inputString):
    r = [inputString.count(i) for i in string.ascii_lowercase]
    
    return r[::-1] == sorted(r)
    
    
print(isBeautifulString(inputString))
