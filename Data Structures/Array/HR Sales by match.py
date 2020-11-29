# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

n = 9
ar = [10, 20, 20, 10, 10, 30, 50, 10, 20]

dict1 = {}

def sockMerchant(n, ar):  
    for i in range(len(ar)):
        if ar[i] in dict1:
            dict1[ar[i]] += 1
        else:
            dict1[ar[i]] = 1

    count = 0
    for key,val in dict1.items():
        count += val // 2
    return sum([ar.count(i)//2 for i in set(ar)])

print(sockMerchant(n, ar))
