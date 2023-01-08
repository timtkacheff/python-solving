from typing import List
import sys


# Given an array of distinct integers arr, find all pairs of elements with the minimum
# absolute difference of any two elements.
#
# Return a list of pairs in ascending order(with respect to pairs), each pair [a, b] follows
#
#     a, b are from arr
#     a < b
#     b - a equals to the minimum absolute difference of any two elements in arr

class Solution:
    def minimumAbsDifference(self, arr: List[int]):
        arr.sort()
        min_diff, out = sys.maxsize, []

        for i in range(0, len(arr) - 1):
            current_diff = abs(arr[i] - arr[i + 1])

            if current_diff < min_diff:
                min_diff = current_diff
                out = [[arr[i], arr[i + 1]]]

            elif current_diff == min_diff:
                out.append([arr[i], arr[i + 1]])

        return out


sol = Solution()

print(sol.minimumAbsDifference([4, 2, 1, 3]))
print(sol.minimumAbsDifference([1, 3, 6, 10, 15]))
print(sol.minimumAbsDifference([3, 8, -10, 23, 19, -4, -14, 27]))
print(sol.minimumAbsDifference([40, 11, 26, 27, -20]))
