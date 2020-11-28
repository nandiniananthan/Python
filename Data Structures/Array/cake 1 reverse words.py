# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

message = [ 'c', 'a', 'k', 'e', ' ',
          'p', 'o', 'u', 'n', 'd', ' ',
          's', 't', 'e', 'a', 'l' ]

OP = 'steal pound cake'

def reverse_words(message):
    n = len(message)
    reverse_ch(message, 0, n-1)
    start = 0
    
    for i in range(n+1):
        if i == n or message[i] == ' ':
            reverse_ch (message, start, i-1)
            start  = i + 1
    return message

def reverse_ch(message,left_index,right_index):
    message = message[left_index:right_index:-1]


print(reverse_words(message))