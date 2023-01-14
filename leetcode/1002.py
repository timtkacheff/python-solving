from typing import List


# Given a string array words, return an array of all characters that show up in all strings within the words
# (including duplicates). You may return the answer in any order.

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        if len(words) < 2:
            return words

        unique_letters = set(words[0])

        res = []

        for letter in unique_letters:
            n = (min([elem.count(letter) for elem in words]))
            if n:
                res += letter * n

        return res
