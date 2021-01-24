# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 09:54:48 2021

@author: nandini.ananthan
"""

value1 = 15
weight1 = 2
value2 = 20
weight2 = 3
maxW = 2

OP = 15

def knapsackLight(value1, weight1, value2, weight2, maxW):
    if not weight1 + weight2 > maxW:
        return value1 + value2
    elif weight2 <= maxW and value2 > value1:
        return value2
    elif weight1 <= maxW:
        return value1
    else:
        return 0


print(knapsackLight(value1, weight1, value2, weight2, maxW))


