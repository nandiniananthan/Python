# -*- coding: utf-8 -*-
"""
Created on Thu Nov 26 01:58:20 2020

@author: nandini.ananthan
"""

matrix = [[1,3,5,7],[10,11,16,20],[23,30,34,50]]
target = 2

Output: True

def searchMatrix(matrix,target):
    for i in matrix:
        for j in i:
            if j == target:
                return True
    return False        

print(searchMatrix(matrix, target))