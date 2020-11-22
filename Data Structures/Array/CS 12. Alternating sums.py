# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:29:59 2020

@author: nandini.ananthan
"""

a = [50, 60, 60, 45, 70]

def alternatingSums(a):
    sum1 = sum2 = 0

    for i in range(len(a)):
        if i % 2== 0:
            sum1 += a[i]
        else:
            sum2 += a[i]

    return [sum1,sum2]



# SOLN 1 #
print(sum(a[::2]),sum(a[1::2]))