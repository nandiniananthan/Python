# -*- coding: utf-8 -*-
"""
Created on Thu Feb 11 19:51:31 2021

@author: nandini.ananthan
"""

matrix = [
    [1,2,3,4],
    [5,0,7,8],
    [6,1,1,2],
    [2,3,4,0]
]

Output = [
    [1,0,3,0],
    [0,0,0,0],
    [6,0,1,0],
    [0,0,0,0]
]

def zeroMatrix(matrix):
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                matrix[i][j] = setNone(matrix, i, j)
            
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == None:
                matrix[i][j] = 0
    return matrix
                

def setNone(matrix, r, c):
     for i in range(len(matrix[r])):
        if matrix[r][i] != 0:
            matrix[r][i] = None
    
     for j in range(len(matrix)):
        if matrix[j][c] != 0:
            matrix[j][c] = None
    
     matrix[r][c] = None
     

print(zeroMatrix(matrix))
            
            
            
            
            
            
            
            
            
            
            