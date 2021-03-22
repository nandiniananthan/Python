# -*- coding: utf-8 -*-
"""
Created on Mon Mar 22 12:15:59 2021

@author: nandini.ananthan
"""

height = [3, 0, 0, 2, 0, 4]

maxL = [1] * len(height) 
maxL[0] = height[0]

for i in range(1, len(height)):
    maxL[i] = max(maxL[i-1], height[i])
print(maxL)

maxR = [1] * len(height) 
maxR[-1] = height[-1]

for i in range(len(height)-2, -1, -1):
    maxR[i] = max(maxR[i+1], height[i])
print(maxR)
        
min_arr = [1] * len(height)
for i in range(len(min_arr)):
    min_arr[i] = min(maxL[i], maxR[i])
print(min_arr)

water = [1] * len(height)
for i in range(len(height)):
    water[i] = min_arr[i] - height[i]
print(water)

print(sum(water))

        
