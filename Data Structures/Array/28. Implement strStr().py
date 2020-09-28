# -*- coding: utf-8 -*-
"""
Created on Mon Sep 28 11:57:30 2020

@author: nandini.ananthan
"""

haystack = "s"
needle = ""

def strStr(self, haystack: str, needle: str) -> int:
    L, n = len(needle), len(haystack)

    for start in range(n - L + 1):
        if haystack[start: start + L] == needle:
            return start
    return -1
        