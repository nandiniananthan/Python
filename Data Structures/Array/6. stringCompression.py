# -*- coding: utf-8 -*-
"""
Created on Tue Feb  2 21:52:04 2021

@author: nandini.ananthan
"""

str1 = "aabcccccaaa"
OP = "a2b1c5a3"

ans = []
count = 1

for i in range(len(str1)-1):
    if str1[i] == str1[i+1]:
        count += 1
    else:
        ans.append(str1[i])
        ans.append(str(count))
        count = 1

ans.append(str1[i])
ans.append(str(count))    
ans = "".join(ans)
print(ans)



    
