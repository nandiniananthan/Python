# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:41:04 2021

@author: nandini.ananthan
"""

head = [3,2,0,-4]
OP = True

def hasCycle(self, head: ListNode) -> bool:
    #curr = head
    dict1 = {}
    while head:
        if head in dict1:
            return True
        dict1[head] = 1
        head = head.next
    return False
