"""
class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        arr1 = []
        
        for i in range(n):
            val = target - nums[i]
            for j in range(i+1,n):
                if nums[j] == val:
                    return i,j
"""
nums = [2, 7, 11, 15]
target = 9
d = {}

for i,n in enumerate(nums):
    m = target-n
    if m in d:
        print(d[m], i)

    else:
        d[n] = i                  