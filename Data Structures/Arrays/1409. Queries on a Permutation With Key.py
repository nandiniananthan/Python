# -*- coding: utf-8 -*-
"""
Created on Mon Jul 13 20:42:00 2020

@author: nandini.ananthan
"""
queries = [3,1,2,1] 
m = 5
P = list(range(1,m+1))
print(P)
arr1= []


for i in range(len(queries)):
    for j in range(len(P)):
        if P[j] == queries[i]:
            P.insert(0,P.pop(j))
            arr1.append(j)
print("the final array is: ",arr1)   
