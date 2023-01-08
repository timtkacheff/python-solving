import math


# Given a positive integer n, find the pivot integer x such that:
#
#     The sum of all elements between 1 and x inclusively equals the sum of all elements between x and n inclusively.
#
# Return the pivot integer x. If no such integer exists, return -1.
# It is guaranteed that there will be at most one pivot index for the given input.

class Solution:
    def pivotInteger(self, n: int) -> int:
        ans = (n*n + n) // 2
        sq = int(math.sqrt(ans))
        if sq * sq == ans:
            return sq
        else:
            return -1


sol = Solution()

print(sol.pivotInteger(4))
