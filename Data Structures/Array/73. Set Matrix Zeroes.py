# -*- coding: utf-8 -*-
"""
Created on Thu Oct  8 18:54:23 2020

@author: nandini.ananthan
"""

matrix = [[1,1,1],[1,0,1],[1,1,1]]
Output= [[1,0,1],[0,0,0],[1,0,1]]

def setZeroes(matrix):
    row = []
    column = []
    R = len(matrix)
    C = len(matrix[0])
    for i in range(R):
        for j in range(C):
            if matrix[i][j] == 0:
                row.append(i)
                column.append(j)
    
    for i in range(R):
        for j in range(C):
            if i in row or j in column:
                matrix[i][j] = 0
    return matrix
            
                
print(setZeroes(matrix))             

