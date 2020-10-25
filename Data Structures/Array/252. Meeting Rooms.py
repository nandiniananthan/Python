# -*- coding: utf-8 -*-
"""
Created on Sun Oct 25 11:56:41 2020

@author: nandini.ananthan
"""

intervals = [[6,10],[13,14],[12,14]]
#OP : false

def canAttendMeetings(intervals):
    intervals = sorted(intervals)
    for i in range(len(intervals)-1):
        if intervals[i][1] > intervals[i+1][0]:
            return False
    return True
    
    
print(canAttendMeetings(intervals))
