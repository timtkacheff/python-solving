from typing import List


# Given an array of n integers nums, a 132 pattern is a subsequence of three integers nums[i],
# nums[j] and nums[k] such that i < j < k and nums[i] < nums[k] < nums[j].
#
# Return true if there is a 132 pattern in nums, otherwise, return false.

class Solution:
    def find132pattern(self, nums: List[int]) -> bool:
        stack = []
        cur_min = nums[0]

        for n in nums[1:]:
            while stack and stack[-1][0] <= n:
                stack.pop()
            if stack and stack[-1][1] < n:
                return True
            stack.append([n, cur_min])
            cur_min = min(cur_min, n)

        return False


sol = Solution()
print(sol.find132pattern([1, 2, 3, 4]))  # -> False
print(sol.find132pattern([3, 1, 4, 2]))  # -> True
print(sol.find132pattern([1, 4, 2, 3]))  # -> True
print(sol.find132pattern([3, 5, 0, 3, 4]))  # -> True
