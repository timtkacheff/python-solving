import math


# Given an integer n, return true if it is a power of two. Otherwise, return false.
#
# An integer n is a power of two, if there exists an integer x such that n == 2^x.

class Solution:

    def isPowerOfTwo(self, n: int):
        if n < 0:
            return False

        return math.isclose(math.log(n, 2), int(math.log(n, 2)), rel_tol=1e-15)


sol = Solution()

print(sol.isPowerOfTwo(536870912))
