# Given a string s which consists of lowercase or uppercase letters,
# return the length of the longest palindrome that can be built with those letters.
#
# Letters are case sensitive, for example, "Aa" is not considered a palindrome here.

class Solution:
    def longestPalindrome(self, s: str):
        counter = {}
        for _, v in enumerate(s):
            if v not in counter:
                counter[v] = 0
            counter[v] += 1

        result = 0
        for value in counter.values():
            result += value // 2 * 2
            if result % 2 == 0 and value % 2 == 1:
                result += 1

        return result


sol = Solution()
print(sol.longestPalindrome("abccccdd"))
