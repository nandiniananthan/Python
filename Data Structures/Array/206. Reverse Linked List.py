# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 19:32:23 2021

@author: nandini.ananthan
"""

Input: 1->2->3->4->5->NULL
Output: 5->4->3->2->1->NULL 

class Solution:
    def reverseList(self, head: ListNode) -> ListNode:
        prev = None
        curr = head
        while curr is not None:
            next = curr.next
            curr.next = prev
            prev = curr
            curr = next
        head = prev
        return head
        

    
    
    