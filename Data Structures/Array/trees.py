# -*- coding: utf-8 -*-
"""
Created on Thu Jan 21 06:29:22 2021

@author: nandini.ananthan
"""

class Node:
    def __init__(self, val):
        self.value = val
        self.LeftChild = None
        self.RightChild = None
        
    def insert(self, data):
        if self.value == data:
            return False
        
        elif self.value > data:
            if self.LeftChild:
                return self.LeftChild.insert(data)
            else:
                self.LeftChild = Node(data)
                return True
        else:
            if self.RightChild:
                return self.RightChild.insert(data)
            else:
                self.RightChild = Node(data)
                return True
    
    def find(self, data):
        if(self.value == data):
            return True
        elif self.value > data:
            if self.LeftChild:
                return self.LeftChild.find(data)
            else:
                return False
        else:
            if self.RightChild:
                return self.RightChild.find(data)
            else:
                return False

    def preorder(self):
        if self:
            print(str(self.value))
            if self.LeftChild:
                self.LeftChild.preorder()
            if self.RightChild:
                self.RightChild.preorder()

    def postorder(self):
        if self:
            if self.LeftChild:
                self.LeftChild.postorder()
            if self.RightChild:
                self.RightChild.postorder()     
            print(str(self.value))
    
    def inorder(self):
        if self:
            if self.LeftChild:
                self.LeftChild.inorder()
            print(str(self.value))
            if self.RightChild:
                self.RightChild.inorder()         
        
        
    
class Tree:
    def __init__(self):
        self.root = None
        
    def insert(self, data):
        if self.root:
            return self.root.insert(data)    
        else:
            self.root = Node(data)
            return True 
        
    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False
    
    def preorder(self):
        print("Preorder")
        self.root.preorder()
    
    def inorder(self):
        print("inorder")
        self.root.inorder()
    
    def postorder(self):
        print("postorder")
        self.root.postorder()
    
    
bst = Tree()
bst.insert(10)
bst.insert(32)
bst.insert(55)
bst.insert(1)
bst.insert(19)
bst.insert(79)
bst.insert(16)
bst.insert(23)
bst.preorder() 
bst.postorder()
bst.inorder()

    
    
    
    
    