# -*- coding: utf-8 -*-
"""
Created on Tue Nov 10 17:11:04 2020

@author: nandini.ananthan
"""

arr1 = [1,2,3,4,5]
arr2 = [1,2,5,7,9]
arr3 = [1,3,4,5,8]

Output: [1,5]

################       dict        ########   
res1 = []
dict1 = {}

for i in range(len(arr1)):
    if arr1[i] in dict1:
        dict1[arr1[i]] += 1
    else:
        dict1[arr1[i]] = 1

for i in range(len(arr2)):
    if arr2[i] in dict1:
        dict1[arr2[i]] += 1
    else:
        dict1[arr2[i]] = 1
        
for i in range(len(arr3)):
    if arr3[i] in dict1:
        dict1[arr3[i]] += 1
    else:
        dict1[arr3[i]] = 1

for key,value in dict1.items():
    if value >= 3:
        res1.append(key)

print(dict1)        
print(res1)



########        list         ############

def arraysIntersection(arr1,arr2,arr3):
    return sorted(list(set(arr1) & set(arr2) & set(arr3)))

print(arraysIntersection(arr1, arr2, arr3))