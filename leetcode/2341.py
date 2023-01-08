from typing import List
from collections import Counter


# You are given a 0-indexed integer array nums. In one operation, you may do the following:
#
#     Choose two integers in nums that are equal.
#     Remove both integers from nums, forming a pair.
#
# The operation is done on nums as many times as possible.
#
# Return a 0-indexed integer array answer of size 2 where answer[0] is the number of pairs that
# are formed and answer[1] is the number of leftover integers in nums after doing the operation
# as many times as possible.

class Solution:

    def numberOfPairs(self, nums: List[int]):  # -> List[int]
        ans = [0] * 2
        counted = Counter(nums)

        for v in counted.values():
            ans[0] += v // 2
            ans[1] += v % 2

        return ans


sol = Solution()
print(sol.numberOfPairs([1, 3, 2, 1, 3, 2, 2]))
print(sol.numberOfPairs([1, 1]))
