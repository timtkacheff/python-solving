from typing import List


# Given an integer array nums of 2n integers, group these integers into n pairs (a1, b1), (a2, b2),
# ..., (an, bn) such that the sum of min(ai, bi) for all i is maximized. Return the maximized sum.

class Solution:
    def arrayPairSum(self, nums: List[int]) -> int:
        nums.sort()

        max_sum = 0

        for i in range(0, len(nums), 2):
            max_sum += nums[i]

        return max_sum


print(Solution().arrayPairSum([1, 2, 3, 4]))
