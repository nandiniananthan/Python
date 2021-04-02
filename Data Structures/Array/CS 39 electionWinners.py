# -*- coding: utf-8 -*-
"""
Created on Fri Apr  2 01:07:32 2021

@author: nandini.ananthan
"""

votes = [2, 3, 5, 2]
k = 2

def electionVotes(votes, k):
    c = 0
    mv = max(votes)
    if k == 0 and votes.count(mv) == 1:
        return 1
    
    for i in votes:
        if i + k > mv:
            c += 1
    return c

print(electionVotes(votes, k))

