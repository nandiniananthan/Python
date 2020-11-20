# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 17:24:08 2020

@author: nandini.ananthan
"""

matrix =    [[0,1,1,2], 
             [0,5,0,0], 
             [2,0,3,3]]
OP = 9

count = 0
no = []
       

for j in range(len(matrix[0])):
    for i in range(len(matrix)):
        if matrix[i][j] != 0:
            count += matrix[i][j]
        else:
            break
print(count)



############     me          ###########

def matrixElementsSum(matrix):
    count = 0
    no = []
        
    for i in range(len(matrix)):
        for j in range(len(matrix[0])):
            if matrix[i][j] == 0:
                no.append(j)
        for k in range(len(matrix[0])):
            if k not in no:
                count += matrix[i][k]
    return (count)
