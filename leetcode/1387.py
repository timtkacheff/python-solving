# The power of an integer x is defined as the number of steps needed to transform x 
# into 1 using the following steps:
#
#     if x is even then x = x / 2
#     if x is odd then x = 3 * x + 1
#
# For example, the power of x = 3 is 7 because 3 needs 7 steps to become 1:
# (3 --> 10 --> 5 --> 16 --> 8 --> 4 --> 2 --> 1).
#
# Given three integers lo, hi and k. 
# The task is to sort all integers in the interval [lo, hi] by the power value in ascending order, 
# if two or more integers have the same power value sort them by ascending order.
#
# Return the kth integer in the range [lo, hi] sorted by the power value.
#
# Notice that for any integer x (lo <= x <= hi) it is guaranteed that x will transform into 1
# using these steps and that the power of x is will fit in a 32-bit signed integer.

class Solution:
    def getKth(self, lo: int, hi: int, k: int):  # -> int:
        cache = {1: 0}
        def calcPower(n):
            if n in cache:
                return cache[n]
            if n % 2 == 0:
                cache[n] = calcPower(n / 2) + 1
            else:
                cache[n] = calcPower(3 * n + 1) + 1
            return cache[n]

        return sorted((calcPower(i), i) for i in range(lo, hi+1))[k-1][1]

sol = Solution()
# print(sol.getKth(12, 15, 2))
print(sol.getKth(7, 11, 4))
