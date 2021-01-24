# -*- coding: utf-8 -*-
"""
Created on Sun Jan 24 12:30:42 2021

@author: nandini.ananthan
"""

b = "a1"
p = "c3"
OP = True

def bishopAndPawn(b, p):
    b=[ord(b[0]),int(b[1])]
    p=[ord(p[0]),int(p[1])]
    return b[1]-b[0]==p[1]-p[0] or sum(b)==sum(p)