# -*- coding: utf-8 -*-
"""
Created on Tue Sep 22 10:13:51 2020

@author: nandini.ananthan
"""

n = 15
arr1 = []

#####  NAIVE APPROACH    ########
'''
for i in range(1,n+1):
    if i%3 == 0 and i%5 == 0:
        arr1.append("FizzBuzz")
    elif i%3 == 0:
        arr1.append("Fizz")
    elif i%5 == 0:
        arr1.append("Buzz")
    else:
        arr1.append(str(i))

print(arr1)
'''
#####     USING HASHMAP    ##########

dict1 = {3:'Fizz', 5:'Buzz'}

for i in range(1,n+1):
    str1 = ''
    for keys in dict1.keys():
        if i % keys == 0:
            str1 += dict1[keys]
    if not str1:
        str1 = str(i)
    
    arr1.append(str1)

print(arr1)