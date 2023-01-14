# Given a string s, reverse the string according to the following rules:
#
#     All the characters that are not English letters remain in the same position.
#     All the English letters (lowercase or uppercase) should be reversed.
#
# Return s after reversing it.

class Solution:
    def reverseOnlyLetters(self, s: str) -> str:
        letters = [c for c in s if c.isalpha()]
        answer = []
        for c in s:
            if c.isalpha():
                answer.append(letters.pop())
            else:
                answer.append(c)
        return "".join(answer)
