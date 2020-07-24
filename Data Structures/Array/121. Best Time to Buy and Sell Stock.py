# -*- coding: utf-8 -*-
"""
Created on Fri Jul 24 11:59:48 2020

@author: nandini.ananthan
"""
"""
prices = [7,6,4,3,1]
Output: 5
max_val = temp = 0

for i in range(len(prices)-1):
    if prices[i] > prices[i+1]:
        temp = prices[i+1]
        print("temp is",temp)
        for j in range(i+2, len(prices)-1):
            print("i+2",prices[i+2])
            if prices[i+2] > temp and prices[i+2] > max_val:
                max_val = prices[i+2]
            else:
                pass
            print("max so far",max_val)
    else:
        print(0)
    print("")
    print("final op is",max_val-temp)
"""
prices = [7,1,5,3,6,4]

def maxProfit(prices):
    maxProfit = 0
    minPrice = float('inf')
    for i in range(len(prices)):
        minPrice = min(minPrice, prices[i])
        maxProfit = max(maxProfit, prices[i]-minPrice)
    return maxProfit  

maxProfit(prices)
    
    
    
        
        
        
        
        
        
        
        
        
        
        
        
        
        