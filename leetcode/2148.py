from typing import List


# Given an integer array nums, return the number of elements that have
# both a strictly smaller and a strictly greater element appear in nums.

class Solution:
    def countElements(self, nums: List[int]) -> int:
        max_num = max(nums)
        min_num = min(nums)
        result = 0

        for i, num in enumerate(nums):
            if max_num > num > min_num:
                result += 1

        return result
