# An integer x is a good if after rotating each digit individually by 180 degrees,
# we get a valid number that is different from x. 
# Each digit must be rotated - we cannot choose to leave it alone.
#
# A number is valid if each digit remains a digit after rotation. For example:
#
#     0, 1, and 8 rotate to themselves,
#     2 and 5 rotate to each other (in this case they are rotated in a different direction, 
#                                   (in other words, 2 or 5 gets mirrored),
#     6 and 9 rotate to each other, and
#     the rest of the numbers do not rotate to any other number and become invalid.
#
# Given an integer n, return the number of good integers in the range [1, n].

class Solution:

    # INFO: Faster solution
    def rotatedDigits(self, n: int) -> int:
        s1 = set([0, 1, 8])
        s2 = set([0, 1, 2, 5, 6, 8, 9])

        def isGood(x):
            digit_set = set([int(i) for i in str(x)])
            return digit_set.issubset(s2) and not digit_set.issubset(s1)

        return sum(isGood(i) for i in range(1, n + 1))

    # INFO: Slower solution

    # def rotatedDigits(self, n: int):  # -> int:
    #     res = 0
    #     for i in range(1, n + 1):
    #         if self._rotate(i) == True:
    #             res += 1
    #
    #     return res
    #
    # def _rotate(self, n: int) -> bool:
    #     good_map = {
    #         "0": "0",
    #         "1": "1",
    #         "2": "5",
    #         "5": "2",
    #         "6": "9",
    #         "8": "8",
    #         "9": "6"
    #     }
    #
    #     digits = list(str(n))
    #     for i in range(len(digits)):
    #         if digits[i] not in good_map:
    #             return False
    #
    #         digits[i] = good_map[digits[i]]
    #
    #     return n != int("".join(digits))


sol = Solution()

print(sol.rotatedDigits(5212))
