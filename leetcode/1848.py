from typing import List


# Given an integer array nums (0-indexed) and two integers target and start,
# find an index i such that nums[i] == target and abs(i - start) is minimized.
# Note that abs(x) is the absolute value of x.
#
# Return abs(i - start).
#
# It is guaranteed that target exists in nums.

class Solution:
    def getMinDistance(self, nums: List[int], target: int, start: int) -> int:
        result = 10**4
        for i, num in enumerate(nums):
            if num == target:
                result = min(abs(i - start), result)

        return result
