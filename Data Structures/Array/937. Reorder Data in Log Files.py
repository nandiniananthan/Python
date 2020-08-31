# -*- coding: utf-8 -*-
"""
Created on Sun Aug 30 19:27:05 2020

@author: nandini.ananthan
"""


logs = ["dig1 8 1 5 1","let1 art can","dig2 3 6","let2 own kit dig","let3 art zero"]


def reorderLogFiles(logs):
    res1, res2 = [], []
    #print("logs is:", logs)
    for log in logs:
        if(log.split()[1].isdigit()):
            res2.append(log) #digits
    
        else:
            res1.append(log.split()) #letters
            
    #print("res1 before sorting", res1)
    res1.sort(key = lambda x : x[0])
    res1.sort(key = lambda x : x[1:])
    #print("res1 after sorting", res1)
    for i in range(len(res1)):
        res1[i] = (" ".join(res1[i]))
    res1.extend(res2)
    return res1

print(reorderLogFiles(logs))
