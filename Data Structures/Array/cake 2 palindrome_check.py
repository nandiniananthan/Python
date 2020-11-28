# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:13:12 2020

@author: nandini.ananthan
"""

the_string = 'aabbcdd'


def has_palindrome_permutation(the_string):
    dict1 = {}
    for i in range(len(the_string)):
        if the_string[i] not in dict1:
            dict1[the_string[i]] =1
        else:
            dict1[the_string[i]] += 1
    
    count = 0
    
    for key,val in dict1.items():
        if val % 2 != 0:
            count += 1
    if count > 1:
        return False
    return True

print(has_palindrome_permutation(the_string))