# -*- coding: utf-8 -*-
"""
Created on Sat Jul 18 17:06:51 2020

@author: nandini.ananthan
"""


digits = [4,3,2,1]
n = len(digits)
carry = 0


for i in range(n-1, -1, -1):       
    if digits[i] == 9:
        while digits[i] == 9:
            digits[i] = 0
            carry = 1
            print(digits[i])
            
    else:
        digits[i] += 1
        break
        
    
    
if digits[0] == 0:       # when there's a 9 at position 0 #
    digits.insert(0,1)
    
print(digits)

    