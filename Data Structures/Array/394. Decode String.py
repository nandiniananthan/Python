# -*- coding: utf-8 -*-
"""
Created on Tue Feb 23 16:43:10 2021

@author: nandini.ananthan
"""

s = "3[a]2[bc]"
Output = "aaabcbc"

class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        curNum = 0 #3
        curString = ''
        for c in s:
            if c == '[':
                stack.append(curString)
                stack.append(curNum)
                curNum = 0
                curString = ''
            elif c == ']':
                num = stack.pop()
                char = stack.pop()
                curString = char + num * curString
                print(curString)
            elif c.isdigit():    
                curNum = curNum*10 + int(c)
            else:
                curString += c
        return curString
    
                
                    
        
        