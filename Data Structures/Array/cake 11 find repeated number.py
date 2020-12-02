# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 16:47:30 2020

@author: nandini.ananthan
"""

numbers = [4, 1, 4, 8, 3, 2, 7, 6, 5]

def find_repeat(numbers):
    dict1 = {}
    for i in range(len(numbers)):
        if numbers[i] in dict1:
            return numbers[i]
        else:
            dict1[numbers[i]] = 1

print(find_repeat(numbers))