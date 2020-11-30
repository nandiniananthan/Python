# -*- coding: utf-8 -*-
"""
Created on Sun Nov 29 15:49:16 2020

@author: nandini.ananthan
"""
list_of_ints = [-10, 1, 3, 2, -10]
OP = 300

def highest_product_of_3(list_of_ints):

  highest = max(list_of_ints[0], list_of_ints[1])
  lowest  = min(list_of_ints[0], list_of_ints[1])
  highest_product_of_2 = list_of_ints[0] * list_of_ints[1]
  lowest_product_of_2  = list_of_ints[0] * list_of_ints[1]
  highest_product_of_3 = list_of_ints[0] * list_of_ints[1] * list_of_ints[2]

  for i in range(2, len(list_of_ints)):
      current = list_of_ints[i]
      highest_product_of_3 = max(highest_product_of_3,
                                 current * highest_product_of_2,
                                 current * lowest_product_of_2)
      highest_product_of_2 = max(highest_product_of_2,
                                 current * highest,
                                 current * lowest)
      lowest_product_of_2 = min(lowest_product_of_2,
                                current * highest,
                                current * lowest)
      highest = max(highest, current)
      lowest = min(lowest, current)

  return highest_product_of_3

print(highest_product_of_3(list_of_ints))