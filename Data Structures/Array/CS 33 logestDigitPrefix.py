# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 10:13:38 2021

@author: nandini.ananthan
"""

import re

inputString = "123aa123"
OP = "123"

def longestDigitsPrefix(inputString):
    return re.findall('$\d+',inputString)
            
print(longestDigitsPrefix(inputString))


def longestDigitsPrefix(inputString):
    digit = ''
    for i in inputString:
        if i.isnumeric():
            digit += i
        else:
            break
        
    return (digit)
            

