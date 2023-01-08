from typing import List
import functools

# The XOR total of an array is defined as the bitwise XOR of all its elements, 
#                                                  or 0 if the array is empty.
#
#     For example, the XOR total of the array [2,5,6] is 2 XOR 5 XOR 6 = 1.
#
# Given an array nums, return the sum of all XOR totals for every subset of nums. 
#
# Note: Subsets with the same elements should be counted multiple times.
#
# An array a is a subset of an array b if a can be obtained from b by 
#                         deleting some (possibly zero) elements of b.

class Solution:

    def subsetXORSum(self, nums: List[int]):
        subsets = self._subsets(nums)
        
        sum = 0

        for i, _ in enumerate(subsets):
            if len(subsets[i]) == 0:
                sum += 0
            elif len(subsets[i]) == 1:
                sum += subsets[i][0]
            else:
                sum += functools.reduce(lambda a,b: a ^ b, subsets[i])

        return sum

    def _subsets(self, nums: List[int]):
        if len(nums) < 1:
            return [[]]

        x = self._subsets(nums[1:])

        return x + [[nums[0]] + y for y in x]


sol = Solution()

print(sol.subsetXORSum([1, 3]))
print(sol.subsetXORSum([5, 1, 6]))
