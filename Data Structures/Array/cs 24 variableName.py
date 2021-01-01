# -*- coding: utf-8 -*-
"""
Created on Fri Jan  1 10:10:34 2021

@author: nandini.ananthan
"""

name = "2w2"

def variableName(name):
        if (name[0].isdigit()):
            return False
        else:
            return all(name[i] == '_' or name[i].isdigit() or name[i].isalpha()  for i in range(0,len(name)))


print(variableName(name))
