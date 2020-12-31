# -*- coding: utf-8 -*-
"""
Created on Thu Dec 31 13:27:10 2020

@author: nandini.ananthan
"""

inputArray = [1, 2, 1]
elemToReplace = 1
substitutionElem = 3

for i in range(len(inputArray)):
    if inputArray[i] == elemToReplace:
        inputArray[i] = substitutionElem

print(inputArray)

def arrayReplace(inputArray, elemToReplace, substitutionElem):
    return [x if x !=elemToReplace else substitutionElem for x in inputArray]

print(arrayReplace(inputArray, elemToReplace, substitutionElem))