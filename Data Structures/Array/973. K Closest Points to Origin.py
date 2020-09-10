# -*- coding: utf-8 -*-
"""
Created on Thu Sep 10 10:19:57 2020

@author: nandini.ananthan
"""
#import collections
import heapq

points = [[3,3],[5,-1],[-2,4]]
K = 2
Output: [[-2,2]]

# sorting #
def kClosest(points,K):
    points.sort(key = lambda P: P[0]**2 + P[1]**2)
    return points[:K]

print(kClosest(points,K))

# heap #
def kClosest(points,K):
	return heapq.nsmallest(K, points, key = lambda x: points[0]**2 + points[1]**2)
