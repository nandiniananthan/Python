# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 12:43:26 2020

@author: nandini.ananthan
"""

stock_prices = [9, 7, 4, 1]
OP = 2

diff = []

for i in range(len(stock_prices)):
    for j in range(i+1 ,len(stock_prices)):
        diff.append(stock_prices[j] - stock_prices[i])

print(diff)        
print(max(diff))