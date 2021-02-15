# -*- coding: utf-8 -*-
"""
Created on Mon Feb 15 01:10:42 2021

@author: nandini.ananthan
"""

intersectVal = 8, listA = [4,1,8,4,5], listB = [5,6,1,8,4,5], skipA = 2, skipB = 3

def getIntersectionNode(self, headA: ListNode, headB: ListNode) -> ListNode:
    Apointer = headA
    Bpointer = headB
    
    while Apointer != Bpointer:
            Apointer = headB if Apointer == None else Apointer.next
            Bpointer = headA if Bpointer == None else Bpointer.next
    
    return Apointer 
