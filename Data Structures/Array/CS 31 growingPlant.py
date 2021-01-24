# -*- coding: utf-8 -*-
"""
Created on Sat Jan 23 18:02:04 2021

@author: nandini.ananthan
"""

upSpeed = 100
downSpeed = 10
desiredHeight = 910



def he(upSpeed, downSpeed, desiredHeight):
    height = count = 0
    while True:
        count += 1
        height += upSpeed
        if height >= desiredHeight:
            return(count)
        height -= downSpeed

print(he(upSpeed, downSpeed, desiredHeight))