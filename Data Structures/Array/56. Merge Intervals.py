# -*- coding: utf-8 -*-
"""
Created on Tue Sep  1 22:21:49 2020

@author: nandini.ananthan
"""

intervals = [[1,3],[2,6],[8,10],[15,18]]
intervals.sort()

i=1
while i < len(intervals):
    if intervals[i][0] <= intervals[i-1][1]:
        intervals[i-1][0] = min(intervals[i][0],intervals[i-1][0])
        intervals[i-1][1] = max(intervals[i][1],intervals[i-1][1])
        intervals.pop(i)
    else:
        i +=  1

print("final output is: ", intervals)