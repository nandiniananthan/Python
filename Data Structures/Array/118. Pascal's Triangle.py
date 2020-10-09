# -*- coding: utf-8 -*-
"""
Created on Fri Oct  9 10:12:27 2020

@author: nandini.ananthan
"""

nums = 5
Output = [
     [1],
    [1,1],
   [1,2,1],
  [1,3,3,1],
 [1,4,6,4,1]
]

triangle = []
for num in range(nums):
    row = [None for _ in range(num+1)]
    row[0], row[-1] = 1,1
    
    for j in range(1,len(row)-1):
        row[j] = triangle[num-1][j-1] + triangle[num-1][j]
    triangle.append(row)

print(triangle)
    