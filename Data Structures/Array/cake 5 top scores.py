# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:30:32 2020

@author: nandini.ananthan
"""

unsorted_scores = [30, 60]
highest_possible_score = 100
op= [60,30]

arr1 = [0] * (highest_possible_score+1)

for score in unsorted_scores:
    arr1[score] += 1

sorted_scores = []

for score in range(len(arr1)-1,-1,-1):
    count = arr1[score]
    
    for time in range(count):
        sorted_scores.append(score)
        
print(sorted_scores)