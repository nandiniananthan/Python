# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 13:06:45 2020

@author: nandini.ananthan
"""

inputArray = ["aba", "aa", "ad", "vcd", "aba"]
output = ["aba", "vcd", "aba"]
arr1=[]

m = len(max(inputArray, key=len))
print((val for val in inputArray if len(val) == m))

