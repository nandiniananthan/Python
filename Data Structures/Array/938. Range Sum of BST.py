# -*- coding: utf-8 -*-
"""
Created on Sun Sep 20 15:59:01 2020

@author: nandini.ananthan
"""

root = [10,5,15,3,7,13,18,1,0,6]
L = 6
R = 10


class Solution:
    def rangeSumBST(self, root):
        def dfs(node):
            if node:
                if L <= node.val <= R:
                    self.ans += node.val
                
                if L < node.val:
                    dfs(node.left)
                
                if node.val < R:
                    dfs(node.right)
                
        self.ans = 0
        dfs(root)
        return self.ans