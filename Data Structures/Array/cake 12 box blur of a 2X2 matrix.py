# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
'''
matrix = [['true', 'false','false','true'], 
         ['false','false','true','false'], 
         ['true','true','false','true']]
'''
matrix = [['true', 'false','false'], 
         ['false','true','false'], 
         ['false','false','false']]

output = [[1, 2, 1],
          [2, 1, 1],
          [1, 1, 1]]

OP = [[0 for i in range(len(matrix[0]))] for j in range(len(matrix))]
print(OP)

for i in range(len(matrix)-1):
    for j in range(len(matrix[0])-1):
        if matrix[i][j] == 'true':
            OP[i-1][j] += 1
            OP[i+1][j] += 1
            OP[i][j-1] += 1
            OP[i][j+1] += 1
            OP[i-1][j-1] += 1
            OP[i+1][j+1] += 1
            OP[i-1][j+1] += 1
            OP[i+1][j-1] += 1
            #OP[i][j] += 1
            print(OP)
        else:
            pass