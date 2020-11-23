# -*- coding: utf-8 -*-
"""
Created on Sun Nov 22 15:33:45 2020

@author: nandini.ananthan
"""

yourLeft = 10
yourRight = 15
friendsLeft = 15
friendsRight = 10

def areEquallyStrong(yourLeft, yourRight, friendsLeft, friendsRight):
    #if (yourLeft == friendsLeft or yourLeft ==  friendsRight) and (yourRight == friendsLeft or yourRight == friendsRight):
     #       return True
    #return False
    return sorted([yourLeft,yourRight]) ==  sorted([friendsLeft,friendsRight])