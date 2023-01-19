from typing import List


# Given an integer array nums and an integer k,
# return the number of non-empty subarrays that have a sum divisible by k.
#
# A subarray is a contiguous part of an array.

class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        result = prefix_sum = 0
        mod_array = [1] + [0] * k
        for num in nums:
            prefix_sum += num
            result += mod_array[prefix_sum%k]
            mod_array[prefix_sum%k] += 1

        return result


sol = Solution()
print(sol.subarraysDivByK([4,5,0,-2,-3,1], 5))  # -> 7
