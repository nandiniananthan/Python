# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:04:14 2021

@author: nandini.ananthan
"""


head = [1,1,2]
Output: [1,2]

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if head == None:
            return head
        
        curr = head
        while curr and curr.next:
            if curr.val  == curr.next.val:
                curr.next = curr.next.next
                #curr = curr.next
            else:
                curr = curr.next    
        return head