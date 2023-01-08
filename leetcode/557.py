# Given a string s, reverse the order of characters in each word within a
# sentence while still preserving whitespace and initial word order.

class Solution:

    def reverseWords(self, s: str) -> str:
        return " ".join([x[::-1] for x in s.split(" ")])


print(Solution().reverseWords("Let's take LeetCode contest"))
