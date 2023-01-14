# Given a string s, return the last substring of s in lexicographical order.

class Solution:
    def lastSubstring(self, s: str) -> str:
        i, j, offset, n = 0, 1, 0, len(s)

        while i + offset < n and j + offset < n:
            if s[i + offset] == s[j + offset]:
                offset += 1
            else:
                if s[i+offset] > s[j+offset]:
                    j += offset + 1
                else:
                    i += offset + 1
                if i == j:
                    j += 1

                offset = 0

        return s[i:]


sol = Solution()
print(sol.lastSubstring("abab"))  # [bab]
print(sol.lastSubstring("leetcode"))  # [tcode]
print(sol.lastSubstring("cacacb"))  # [cb]
