# -*- coding: utf-8 -*-
"""
Created on Thu Feb 18 16:27:14 2021

@author: nandini.ananthan
"""


head = [1,2,3,3,4,4,5]
Output: [1,2,5]

class Solution:
    def deleteDuplicates(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
            
        if head.val == head.next.val:
            while head.next and head.val == head.next.val:
                head = head.next
            return self.deleteDuplicates(head.next)
        else:
            head.next = self.deleteDuplicates(head.next)
            return head
                
        