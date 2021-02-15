# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 15:28:21 2021

@author: nandini.ananthan
"""

head = [1,4,3,2,5,2]
x = 3
Output = [1,2,2,4,3,5]

class Solution:
    def partition(self, head: ListNode, x: int) -> ListNode:
        before = before_head = ListNode(0)
        after = after_head = ListNode(0)
        
        while head:
            if head.val < x:
                before.next = head
                before = before.next
            else:
                after.next = head
                after = after.next
            
            head = head.next
        
        after.next = None
        before.next = after_head.next
        
        return before_head.next