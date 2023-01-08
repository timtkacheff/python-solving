# Given two strings first and second,
# consider occurrences in some text of the form "first second third",
# where second comes immediately after first, and third comes immediately after second.
#
# Return an array of all the words third for each occurrence of "first second third".


class Solution:
    # O(n) time
    # O(n) space
    def findOccurencies(self, text: str, first: str, second: str):
        text_split = text.split(" ")

        result = []

        for i in range(len(text_split) - 2):
            if text_split[i] == first and text_split[i + 1] == second:
                result.append(text_split[i + 2])

        return result


sol = Solution()
print(sol.findOccurencies("we will we will rock you", "we", "will"))
