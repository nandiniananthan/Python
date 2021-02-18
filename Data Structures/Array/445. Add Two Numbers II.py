# -*- coding: utf-8 -*-
"""
Created on Wed Feb 17 16:04:49 2021

@author: nandini.ananthan
"""

Input: (7 -> 2 -> 4 -> 3) + (5 -> 6 -> 4)
Output: 7 -> 8 -> 0 -> 7

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
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        dummy = ListNode()
        curr = dummy
        carry = 0
        l1 = self.reverseList(l1)
        l2 = self.reverseList(l2)
        
        while l1 or l2 or carry:
            v1 = l1.val if l1 else 0
            v2 = l2.val if l2 else 0
            
            v = v1 + v2 + carry
            carry = v // 10
            v = v % 10
            curr.next = ListNode(v)
            
            curr = curr.next
            l1 = l1.next if l1 else None
            l2 = l2.next if l2 else None
        
        dummy.next = self.reverseList( dummy.next)
        return dummy.next
        