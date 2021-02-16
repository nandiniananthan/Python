# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 17:17:14 2021

@author: nandini.ananthan
"""

l1 = [2,4,3]
l2 = [5,6,4]
Output: [7,0,8]

class Solution:
    def removeNthFromEnd(self, head: ListNode, n: int) -> ListNode:        
        len1 = 0
        temp = head
        while temp:
            len1 += 1
            temp = temp.next
    
        if len1 == n:
            return head.next
        
        curr = head
        count = 0
        
        n = len1 - n + 1 
        while curr:
            count += 1
            if count + 1 == n:
                curr.next = curr.next.next
                return head
            curr = curr.next
        return head