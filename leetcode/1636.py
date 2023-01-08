from typing import Counter, List
import itertools


# Given an array of integers nums,
# sort the array in increasing order based on the frequency of the values. 
# If multiple values have the same frequency, sort them in decreasing order.
#
# Return the sorted array.

class Solution:

    def frequencySort(self, nums: List[int]):
        nums.sort(reverse=True)
        count = {}
        for _, val in enumerate(nums):
            if val not in count.keys():
                count[val] = 1
            else:
                count[val] += 1

        result = []

        for key, val in count.items():
            result.append([key] * val)

        result.sort(key=len)
        
        result = list(itertools.chain(*result))

        return result

    def frequencySortFaster(self, nums: List[int]) -> List[int]:
        counter = Counter(nums)
        return sorted(nums, key=lambda x: (counter[x], -x))

sol = Solution()

print(sol.frequencySortFaster([1, 1, 2, 2, 2, 3]))
print(sol.frequencySort([2, 3, 1, 3, 2]))
