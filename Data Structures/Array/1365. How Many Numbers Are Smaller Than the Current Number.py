# -*- coding: utf-8 -*-
"""
Created on Fri Nov  6 18:41:34 2020

@author: nandini.ananthan
"""

nums = [7,7,7,7]
Output: [4,0,1,1,3]

n = len(nums)
ans = []


for i in range(n):
    count = 0
    for j in range(n):
        if nums[j] < nums[i]  and i != j:
            count += 1
    ans.append(count)
    print(ans)