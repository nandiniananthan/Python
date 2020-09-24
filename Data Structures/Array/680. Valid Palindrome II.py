# -*- coding: utf-8 -*-
"""
Created on Wed Sep 23 19:59:39 2020

@author: nandini.ananthan
"""
#######   using two pointer    ######
s = "absca"

def palindrome(s):
    l = 0
    r = len(s)-1
    while l < r:
        if s[l] == s[r]:
            l += 1
            r -= 1
        else:
            return s[l:r] ==  s[l:r][::-1] or s[l+1:r+1] ==  s[l+1:r+1][::-1]
    return True

print(palindrome(s))


######  brute-force( time limit exceeded)    #########

def palindrome(s):
    if s == s[::-1]:
        return True
    else:
        s1 = s
        for i in range(len(s1)):
            s1 = s1[:i] + s1[i+1:]
            if s1 == s1[::-1]:
                return True
            s1 = s
    return False