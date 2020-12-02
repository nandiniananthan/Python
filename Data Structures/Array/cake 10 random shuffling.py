# -*- coding: utf-8 -*-
"""
Created on Mon Nov 30 10:48:43 2020

@author: nandini.ananthan
"""
import random

sample_list = [1, 2, 3, 4, 5]


def random_get(floor,ceiling):
    return random.randrange(floor,ceiling)

def shuffle(sample_list):
    if len(sample_list) <= 1:
        return sample_list
        
    n = len(sample_list)
    for i in range(n-1):
        index_to_be_shuffled = random_get(i, n)
        if index_to_be_shuffled != i:
            sample_list[i] , sample_list[index_to_be_shuffled] = sample_list[index_to_be_shuffled], sample_list[i]
    

print(shuffle(sample_list))
