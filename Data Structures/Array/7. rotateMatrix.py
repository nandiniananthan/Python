# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 22:10:40 2021

@author: nandini.ananthan
"""

IP = [[ 5, 1, 9,11],
      [ 2, 4, 8,10],
      [13, 3, 6, 7],
      [15,14,12,16]]

OP =   [[15,13, 2, 5],
        [14, 3, 4, 1],
        [12, 6, 8, 9],
        [16, 7,10,11]]

def rotateMatrix(matrix):
    # Transpose the Matrix
    for i in range(len(matrix)):
        for j in range(i + 1, len(matrix)):
            # Switch the row and column indices
            matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

    # Reverse every row
    for r in range(len(matrix)):
        for i in range(len(matrix[r]) // 2):
            # oppI is the opposing index to i
            oppI = len(matrix[r]) - 1 - i
            matrix[r][i], matrix[r][oppI] = matrix[r][oppI], matrix[r][i]
            
            
    
        
