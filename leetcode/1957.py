# A fancy string is a string where no three consecutive characters are equal.
#
# Given a string s, delete the minimum possible number of characters from s to make it fancy.
#
# Return the final string after the deletion. It can be shown that the answer will always be unique.

class Solution:

    def makeFancyString(self, s: str) -> str:
        chars = [*s]
        count = 1
        for i in range(len(chars) - 1):
            if chars[i] == chars[i + 1]:
                count += 1
            else:
                count = 1

            if count > 2:
                chars[i] = ''

        return ''.join(chars)


sol = Solution()

print(sol.makeFancyString("leeetcode"))
