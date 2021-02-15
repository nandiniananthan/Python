# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 17:25:09 2021

@author: nandini.ananthan
"""

Input: 1->2
Output: false

class Solution:
    def isPalindrome(self, head: ListNode) -> bool:
        arr1 = []
        curr = head
        while curr is not None:
            arr1.append(curr.val)
            curr = curr.next
        return arr1 == arr1[::-1]
