from typing import List


# Given an integer array nums sorted in non-decreasing order,
# return an array of the squares of each number sorted in non-decreasing order.

class Solution:
    def sortedSquares(self, nums: List[int]):
        left = 0
        right = len(nums) - 1

        res = [0 for _ in nums]

        for i in range(len(nums) - 1, -1, -1):
            if (abs(nums[right]) > abs(nums[left])):
                res[i] = nums[right] * nums[right]
                right -= 1
            else:
                res[i] = nums[left] * nums[left]
                left += 1

        return res


sol = Solution()

print(sol.sortedSquares([-4, -1, 0, 3, 10]))
