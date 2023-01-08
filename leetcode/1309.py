# You are given a string s formed by digits and '#'.
# We want to map s to English lowercase characters as follows:
#
#     Characters ('a' to 'i') are represented by ('1' to '9') respectively.
#     Characters ('j' to 'z') are represented by ('10#' to '26#') respectively.
#
# Return the string formed after mapping.
#
# The test cases are generated so that a unique mapping will always exist.

class Solution:
    def freqAlphabets(self, s: str) -> str:
        i = len(s) - 1
        res = []

        while i >= 0:
            if s[i] == '#':
                char = s[i - 2] + s[i - 1]
                res.append(chr(96 + int(char)))
                i -= 3
            else:
                char = s[i]
                res.append(chr(96 + int(char)))
                i -= 1

        return "".join(res[::-1])


sol = Solution()

print(sol.freqAlphabets('1326#'))
