# -*- coding: utf-8 -*-
"""
Created on Fri Oct 23 11:11:36 2020

@author: nandini.ananthan
"""

s = "226"
Output: 2

def numDecodings(s):
    if not s: 
        return 0
    
    dp = [0 for x in range(len(s)+1)]
    dp[0] = 1
    dp[1] = 1 if 0 < int(s[0]) <= 9 else 0
    
    for i in range(2, len(s)+1):
        if 0 < int(s[i-1:i]) <= 9:
            dp[i] += dp[i-1]
        
        if 10 <= int(s[i-2:i]) <= 26:
            dp[i] += dp[i-2]
    
    return dp[len(s)]
        
print(numDecodings(s))