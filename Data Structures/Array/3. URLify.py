# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 12:45:30 2021

@author: nandini.ananthan
"""

str1 = "Mr John Smith"
OP = "abc%20def"

for i in range(len(str1)):
    if str1[i] == " ":
        #print(i)
        str1 = str1.replace(str1[i],"%20")
      
print(str1)

