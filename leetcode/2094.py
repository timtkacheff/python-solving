from typing import List


# You are given an integer array digits, where each element is a digit. The array may contain duplicates.
#
# You need to find all the unique integers that follow the given requirements:
#
#     The integer consists of the concatenation of three elements from digits in any arbitrary order.
#     The integer does not have leading zeros.
#     The integer is even.
#
# For example, if the given digits were [1, 2, 3], integers 132 and 312 follow the requirements.
#
# Return a sorted array of the unique integers.

class Solution:
    def findEvenNumbers(self, digits: List[int]) -> List[int]:

        occurrences = {x: 0 for x in digits}

        for num in digits:
            occurrences[num] += 1

        possible_numbers = [x for x in range(100, 999, 2)]
        result = []

        for i, num in enumerate(possible_numbers):
            for digit in str(num):
                if int(digit) not in digits:
                    break
            else:
                test_occur = {int(x): 0 for x in str(num)}
                for digit in str(num):
                    test_occur[int(digit)] += 1

                for k, v in test_occur.items():
                    if v > occurrences[k]:
                        break
                else:
                    result.append(possible_numbers[i])

        return result
