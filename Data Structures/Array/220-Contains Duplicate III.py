
nums = [1,2,3,1]
k = 3
t = 0

class Solution:
    def containsNearbyAlmostDuplicate(self, nums):
       
        num_len = len(nums)

        #if t == 0 and len(nums) == len(set(nums)):
         #   return False

        for idx,val in enumerate(nums):
            for j in range(idx+1, min(idx+1+k, num_len)):
                if abs(val - nums[j]) <= t:
                    return True
        return False
