# -*- coding: utf-8 -*-
"""
Created on Tue Jul 28 19:04:57 2020

@author: nandini.ananthan
"""

nums1 = [1,2,3,0,0,0] 
nums2 = [2,5,6]
Output: [1,2,2,3,5,6]
m = 3
n = 3

####   Approach 1 - brute force  ##

nums1[:] = sorted(nums1[:m] + nums2)



####   Approach 2 : Two pointers / Start from the beginning   ###

nums1_copy = nums1[:m] 
nums1[:] = []

# Two get pointers for nums1_copy and nums2.
p1 = 0 
p2 = 0

# Compare elements from nums1_copy and nums2
# and add the smallest one into nums1.
while p1 < m and p2 < n: 
    if nums1_copy[p1] < nums2[p2]: 
        nums1.append(nums1_copy[p1])
        p1 += 1
    else:
        nums1.append(nums2[p2])
        p2 += 1

# if there are still elements to add
if p1 < m: 
    nums1[p1 + p2:] = nums1_copy[p1:]
if p2 < n:
    nums1[p1 + p2:] = nums2[p2:]
    
    
    
##    Approach 3 : Two pointers / Start from the end  ##
    
p1 = m-1
p2 = n-1
p = m+n-1

while p1>=0 and p2>=0:
    if nums1[p1] < nums2[p2]:
        nums1[p] = nums2[p2]
        p2 -= 1
    
    else:
        nums1[p] = nums1[p1]
        p1 -= 1
        
    p -= 1

# add missing elements from nums2 
nums1[:p2 + 1] = nums2[:p2 + 1]
print(nums1)

