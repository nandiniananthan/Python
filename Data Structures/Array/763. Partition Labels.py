# -*- coding: utf-8 -*-
"""
Created on Mon Oct 19 16:49:30 2020

@author: nandini.ananthan
"""

S = "ababcbacadefegdehijhklij"
Output = [9,7,8]

dict1 = {}

for idx,val in enumerate(S):
    dict1[val] = idx
    
print(dict1)

start,end = 0,0
ans = []

for idx,val in enumerate(S):
    end = max(dict1[val],end)
    #print(end)
    if idx == end:
        curr_length = end - start +1
        ans.append(curr_length)
        start = idx+1
#print(ans)
        
