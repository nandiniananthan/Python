# -*- coding: utf-8 -*-
"""
Created on Tue Jan 19 20:30:08 2021

@author: nandini.ananthan
"""

inputString = "var_1__Int"

        
def firstDigit(inputString):
    for ele in inputString:
        if ele.isnumeric():
            return ele

print(firstDigit(inputString))


    