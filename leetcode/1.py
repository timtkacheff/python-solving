from typing import List


# Given an array of integers nums and an integer target,
# return indices of the two numbers such that they add up to target.
#
# You may assume that each input would have exactly one solution,
# and you may not use the same element twice.
#
# You can return the answer in any order.

class Solution:
    def twoSum(self, nums: List[int], target: int):
        visited = {}
        for i, _ in enumerate(nums):
            # x1 + x2 + x3 ... Xn
            # Xa + Xb = target -> Xa = target - Xb
            x_a = target - nums[i]

            if x_a in visited:
                return [visited[x_a], i]
            else:
                visited[nums[i]] = i


sol = Solution()

print(sol.twoSum([2, 7, 11, 15], 9))
