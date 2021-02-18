# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 00:31:55 2021

@author: nandini.ananthan
"""

head = [1,2,3,4]
Output = [2,1,4,3]


class Solution:
    def swapPairs(self, head: ListNode) -> ListNode:
        curr = ListNode(-1)
        curr.next = head
        
        prev_node = curr
        
        while head and head.next:
            first = head
            second = head.next
            
            prev_node.next = second
            first.next = second.next
            second.next = first
            
            prev_node = first
            head = first.next
        
        return curr.next
    