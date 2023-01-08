# Given two non-negative integers low and high.
# Return the count of odd numbers between low and high (inclusive).

class Solution:
    def countOdds(self, low: int, high: int) -> int:
        if (low & 1) == 0:
            low += 1

        return 0 if low > high else (high - low) // 2 + 1

sol = Solution()
print(sol.countOdds(3, 7))
