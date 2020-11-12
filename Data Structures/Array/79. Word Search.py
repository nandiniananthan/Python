# -*- coding: utf-8 -*-
"""
Created on Thu Nov 12 15:45:10 2020

@author: nandini.ananthan
"""

board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]]
word = "ABCCED"
Output = True

class Solution:
    def exist(self, board,  word):
        self.rows = len(board)
        self.column = len(board[0])
        self.board = board
        
        for row in range(len(board)):
            for column in range(len(board[0])):
                if self.backtrack(row,column,word):
                    return True
        return False
    
    def backtrack(self,row,col,word):
        if len(word) == 0:
            return True
        
        if row < 0 or col < 0 or row == self.rows or col == self.column or self.board[row][col] != word[0]:
            return False
        
        ret = False
        self.board[row][col] = '#'
        '''
        ret = self.backtrack(row+1, col, word) or self.backtrack(row-1, col, word) or self.backtrack(row, col+1, word) or self.backtrack(row, col-1, word)
        '''
        for rowOffset, colOffset in [(0, 1), (1, 0), (0, -1), (-1, 0)]:
            ret = self.backtrack(row + rowOffset, col + colOffset, word[1:])
            # break instead of return directly to do some cleanup afterwards
            if ret: break
        self.board[row][col] = word[0]
        return ret
        