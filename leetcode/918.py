from typing import List


# Given a circular integer array nums of length n,
# return the maximum possible sum of a non-empty subarray of nums.
#
# A circular array means the end of the array connects to the beginning of the array.
# Formally, the next element of nums[i] is nums[(i + 1) % n]
# and the previous element of nums[i] is nums[(i - 1 + n) % n].
#
# A subarray may only include each element of the fixed buffer nums at most once.
# Formally, for a subarray nums[i], nums[i + 1], ..., nums[j],
# there does not exist i <= k1, k2 <= j with k1 % n == k2 % n.

class Solution:
    def maxSubarraySumCircular(self, nums: List[int]) -> int:
        sumNums = sum(nums)
        maxValue = -3 * 10**4
        minValue = 3 * 10**4
        currMax = 0
        currMin = 0
        for num in nums:
            currMax += num
            currMin += num
            if currMin < minValue:
                minValue = currMin
            if currMax > maxValue:
                maxValue = currMax
            if currMin > 0:
                currMin = 0
            if currMax < 0:
                currMax = 0

        return max(maxValue, sumNums - minValue) if maxValue > 0 else maxValue


sol = Solution()
print(sol.maxSubarraySumCircular([1, -2, 3, -2]))  # out -> 3 (subarray: [3])
print(sol.maxSubarraySumCircular([5, -3, 5]))  # out -> 10 (subarray: [5, 5])
print(sol.maxSubarraySumCircular([-3, -2, -3]))  # out -> -2 (subarray: [-2])
