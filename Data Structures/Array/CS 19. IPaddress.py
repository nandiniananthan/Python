# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""

inputString = "172.16.254.1"

def isIPv4Address(inputString):
    nums = inputString.split(".")
    return len(nums) == 4 and all(num.isdigit() and (0 <= int(num) <= 255) and (num[0] != "0" or num == "0") for num in nums)

print(isIPv4Address(inputString))