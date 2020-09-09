# -*- coding: utf-8 -*-
"""
Created on Mon Sep  7 23:02:48 2020

@author: nandini.ananthan
"""

import collections
import heapq

words = ["i", "love", "leetcode", "i", "love", "coding"]
k = 2

def topKFrequent( words, k):
   count = collections.Counter(words)
   print(count)
   heap = [(-freq, word) for word, freq in count.items()]
   print(heap)
   heapq.heapify(heap)
   return [heapq.heappop(heap)[1] for _ in range(k)]

print(topKFrequent(words,k))
