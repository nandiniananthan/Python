# -*- coding: utf-8 -*-
"""
Created on Thu Nov 19 11:56:04 2020

@author: nandini.ananthan
"""

sequence = [1, 3, 2]
Op = True

def almostIncreasingSequence(sequence):
    j = bad(sequence)
    if j == -1:
        return True
    else:
        if bad(sequence[j-1:j] + sequence[j+1:]) == -1:
            return True
        if bad(sequence[j:j+1] + sequence[j+2:]) == -1:
            return True
    return False
    

def bad(test_seq):
    if len(test_seq) <= 2:
        if test_seq[0] < test_seq[1]:
            return -1
    
    else:
        for i in range(len(test_seq)-1):
            if test_seq[i] >= test_seq[i+1]:
                return i
        return -1
        

print(almostIncreasingSequence(sequence))
