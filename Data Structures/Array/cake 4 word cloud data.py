# -*- coding: utf-8 -*-
"""
Created on Fri Nov 27 22:59:08 2020

@author: nandini.ananthan
"""

input_string = 'I like. cake? cake'

input_string = input_string.lower()
print(input_string)

def split_words(input_string):
    curr_word_start = 0
    curr_word_length = 0
    words = []
    
    for i,char in enumerate(input_string):
        if char.isalpha():
            if curr_word_length == 0:
                curr_word_start = i
            curr_word_length += 1
        else:
            word = input_string[curr_word_start : curr_word_start + curr_word_length]
            words.append(word)
            curr_word_length = 0
    return words        

words = split_words(input_string)
print(words)

dict1 = {}
  
def add_to_dict(word):
    if word in dict1:
        dict1[word] += 1
    else:
        dict1[word] = 1
    return dict1

for word in wor
