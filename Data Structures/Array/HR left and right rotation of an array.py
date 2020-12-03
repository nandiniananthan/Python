# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = 5
d = 2
a = [1, 2, 3, 4, 5]
OP = [4,5,1,2,3]


#################        right rotation         ##############
for i in range(d):
    a.insert(0, a.pop(n-1))
    print(a)
    
    
#################        left rotation         #################
    
for i in range(d):
    a.append(a.pop(0))
print(a)