# -*- coding: utf-8 -*-
"""
Created on Tue Jul 14 19:59:42 2020

@author: nandini.ananthan
"""

prices = [10,1,1,6]
for i in range(len(prices)):
    for j in range(i+1,len(prices)):
        if prices[j] <= prices[i]:
            prices[i] = prices[i] - prices[j]
            print(prices[i])
            break

print(prices)
