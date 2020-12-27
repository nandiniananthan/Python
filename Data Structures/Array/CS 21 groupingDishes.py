# -*- coding: utf-8 -*-
"""
Created on Sun Dec 27 20:24:26 2020

@author: nandini.ananthan
"""

dishes =[["Salad", "Tomato", "Cucumber", "Salad", "Sauce"],
        ["Pizza", "Tomato", "Sausage", "Sauce", "Dough"],
        ["Quesadilla", "Chicken", "Cheese", "Sauce"],
        ["Sandwich", "Salad", "Bread", "Tomato", "Cheese"]]

d = {}

for l in dishes:
    dish = l[0]
    for i in l[1:]:
        if i not in d:
            d[i] = [dish]
        else:
            d[i] += [dish]
    
print(d)

out = []


for i in sorted(d):
    if len(d[i]) > 1:
        out += [[i] + sorted(d[i])]

print(out)

