# -*- coding: utf-8 -*-
"""
Created on Sat Feb 13 01:22:35 2021

@author: nandini.ananthan
"""



class Node(object):
    def __init__(self, value):
        self.value = value
        self.next = None
    
class LinkedList(object):
    def __init__(self, head = None):
        self.head = head
    
    def insertNode(self, data):
        node = Node(data)
        node.next = self.head
        self.head = node
    
    def displayList(self):
        current = self.head
        while current:
            print(current.value, end="->")
            current = current.next
            
    def delete_duplicates(self):

        current = self.head
        # This is require to keep track of the prev Node
        prev = None
        duplicate_dict = dict()
        while current:
            if current.value not in duplicate_dict:
                duplicate_dict[current.value] = None
                # Track the prev Node
                prev = current
            else:
                # When a duplicate is found assign prev Node's next to current's next
                prev.next = current.next

            current = current.next
        
    def removeDuplicates(self):
        items = set()
        items.add(self.head.value)
        cur = self.head
        while cur and cur.next:
            if cur.next.value in items:
                cur.next = cur.next.next
            else:
                items.add(cur.next.value)
                cur = cur.next
        return self.head
        

l = LinkedList()
l.insertNode(25)
l.insertNode(35)
l.insertNode(15)
l.insertNode(32)
l.insertNode(25)
l.insertNode(80)
l.insertNode(15)
l.displayList()
#l.delete_duplicates()
l.removeDuplicates()
print()
l.displayList()


        
