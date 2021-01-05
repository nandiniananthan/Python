# -*- coding: utf-8 -*-
"""
Created on Tue Jan  5 13:20:53 2021

@author: nandini.ananthan
"""

deposit = 100
rate = 20
threshold = 170

def depositProfit(deposit, rate, threshold):
    ans = 0
    while deposit < threshold:
        deposit += ((rate/100) * deposit)
        ans += 1 
    return ans

