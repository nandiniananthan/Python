# -*- coding: utf-8 -*-
"""
Created on Sat Nov 21 21:35:57 2020

@author: nandini.ananthan
"""

picture = ["abc",
           "ded"]

OP = ["*****",
      "*abc*",
      "*ded*",
      "*****"]

def addBorder(picture):
    n = len(picture[0])+2
    for i in range(len(picture)):
        picture[i] = '*'+picture[i]+'*'
    
        
    picture.insert(0,'*'*n)
    picture.insert(len(picture),'*'*n)
    return (picture)


print(addBorder(picture))