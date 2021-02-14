# -*- coding: utf-8 -*-
"""
Created on Sun Feb 14 12:02:49 2021

@author: nandini.ananthan
"""

def deleteNode(node):
    node.val = node.next.val
    node.next = node.next.next
    