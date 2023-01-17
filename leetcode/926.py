# A binary string is monotone increasing if it consists of some number of 0's (possibly none),
# followed by some number of 1's (also possibly none).
#
# You are given a binary string s. You can flip s[i] changing it from 0 to 1 or from 1 to 0.
#
# Return the minimum number of flips to make s monotone increasing.


class Solution:
    def minFlipsMonoIncr(self, s: str):  # -> int:
        res = 0
        count = 0

        for c in s:
            if c == '1':
                count += 1
            else:
                res = min(res + 1, count)

        return res



sol = Solution()
print(sol.minFlipsMonoIncr("0101100011"))  # 3
print(sol.minFlipsMonoIncr("00110"))  # 1
print(sol.minFlipsMonoIncr("010110"))  # 2
print(sol.minFlipsMonoIncr("00011000"))  # 2
