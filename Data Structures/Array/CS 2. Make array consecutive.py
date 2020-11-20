# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

statues = [6, 2, 3, 8]

n = len(statues)
statues.sort()

print(statues)
count = 0

for i in range(statues[-1] - statues[0]):
    if statues[i]+1 != statues[i+1]:
        statues.insert(i+1, statues[i]+1)
        count += 1
print(count)
        #break

