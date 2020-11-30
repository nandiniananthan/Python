# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

flight_length = 90
movie_lengths  = [20,20,60,20]

dict1 = {}

def flight_func(flight_length, movie_lengths):
    for i in range(len(movie_lengths)):
        if flight_length - movie_lengths[i] in dict1:
            return True
        dict1[movie_lengths[i]] = 1
    return False

print(flight_func(flight_length, movie_lengths))    
