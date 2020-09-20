# -*- coding: utf-8 -*-
"""
Created on Fri Sep 18 09:39:49 2020

@author: nandini.ananthan
"""

matrix = [[0, 1, 1, 2], 
          [0, 5, 0, 0], 
          [2, 0, 3, 3]]

count = 0
r = len(matrix)
c = len(matrix[0])

for i in range(c):
    for j in range(r):
        #print(i,j)
        if matrix[j][i] != 0:
            count+=matrix[j][i]
            print(matrix[j][i])
        else:
            break
print(count)
'''
r = len(m)
c = len(m[0])
total=0
for j in range(c):
    for i in range(r):
        if m[i][j]!=0:
            total+=m[i][j]
        else:
            break
print(total)
'''
