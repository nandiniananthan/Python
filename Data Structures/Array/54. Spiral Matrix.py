# -*- coding: utf-8 -*-
"""
Created on Mon Nov  2 23:09:18 2020

@author: nandini.ananthan
"""

matrix = [
 [ 1, 2, 3 ],
 [ 4, 5, 6 ],
 [ 7, 8, 9 ]
]

Output: [1,2,3,6,9,8,7,4,5]

def spiralOrder(matrix):
    ans = []
    if matrix == []:
        return matrix
          
    top, left = 0,0
    bottom = len(matrix)-1
    right = len(matrix[0])-1
    
    while left<right and top<bottom:
        for j in range(left,right):
            ans.append(matrix[top][j])
        #top += 1
        for i in range(top,bottom):
            ans.append(matrix[i][right])
        #right -= 1
        for i in range(right,left,-1):
            ans.append(matrix[bottom][i])
        #bottom -= 1
        for i in range(bottom,top,-1):
            ans.append(matrix[i][left])
        left += 1
        right -= 1
        top += 1
        bottom -=1 
    
    if left == right and top == bottom:
    	ans.append(matrix[top][left])
    
    elif left == right:
        for i in range(top, bottom + 1):
       		ans.append(matrix[i][left])
    
    elif top == bottom:
       	for i in range(left, right + 1):
       		ans.append(matrix[top][i])
                       
                       
    return(ans)

print(spiralOrder(matrix))
