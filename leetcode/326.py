import math


# Given an integer n, return true if it is a power of three. Otherwise, return false.
#
# An integer n is a power of three, if there exists an integer x such that n == 3^x.

class Solution:
    def isPowerOfThree(self, n: int):
        if n < 0:
            return False
        n = abs(n)
        x = math.log(n, 3)
        return math.isclose(x, math.ceil(x), rel_tol=1e-15)

    # Since -2^31 <= n <= 2^31 - 1, 3^19 is the biggest power of 3 that fit this constraint
    def isPowerOfThreeFaster(self, n: int):
        return n > 0 and 3 ** 19 % n == 0


sol = Solution()

print(sol.isPowerOfThree(243))
print(sol.isPowerOfThree(9))
