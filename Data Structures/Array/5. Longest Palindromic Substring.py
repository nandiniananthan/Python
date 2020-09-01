# -*- coding: utf-8 -*-
"""
Created on Mon Aug 31 14:30:38 2020

@author: nandini.ananthan
"""

s = "babad"

class Solution:
    def longestPalindrome(self,s):
        largestPalindrome = ""
        
        for i in range(len(s)):
            palOdd = self.largestPalindromeIndex(s,i,i)
            palEven = self.largestPalindromeIndex(s,i,i+1)
            
            largerPalindrome = palOdd if len(palOdd) > len(palEven) else palEven
            largestPalindrome = largestPalindrome if len(largestPalindrome) > len(largerPalindrome) else largerPalindrome
            
    def largestPalindromeIndex(self,s,left,right):
        leftindex = 0
        rightIndex = 0
        
        while left <= 0 and right >= len(s):
            if s[left] == s[right]:
                leftindex = left
                rightIndex = right
                
            else:
                break
            
            left -= 1
            right += 1
            return s[leftindex:rightIndex+1] 
            
            
            
            
            
            
            