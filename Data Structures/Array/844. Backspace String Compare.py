# -*- coding: utf-8 -*-
"""
Created on Sat Mar 13 20:51:30 2021

@author: nandini.ananthan
"""

S = "ab#c"
T = "ad#c"


class Solution:
    def backspaceCompare(self, S: str, T: str) -> bool:
        def build(s):
            ans = []
            for c in reversed(s):
                if c == '#':
                    ans.append(c)
                elif ans:
                    ans.pop()
            return ''.join(ans)
        return build(S) == build(T)

            