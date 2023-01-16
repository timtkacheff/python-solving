from typing import List


# You are given an array of non-overlapping intervals
# where intervals[i] = [starti, endi] represent the start and the end of the ith interval
# and intervals is sorted in ascending order by starti.
# You are also given an interval newInterval = [start, end]
# that represents the start and end of another interval.
#
# Insert newInterval into intervals such that intervals is still sorted in ascending
# order by starti and intervals still does not have any overlapping intervals
# (merge overlapping intervals if necessary).
#
# Return intervals after the insertion.

class Solution:
    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
        if not intervals:
            return [newInterval]

        inserted = False
        for i, interval in enumerate(intervals):
            if interval[0] > newInterval[0]:
                intervals.insert(i, newInterval)
                inserted = True
                break

        if not inserted:
            intervals.append(newInterval)

        n = len(intervals) 
        res = []
        i = 0
        while i < n:
            current = intervals[i]

            while i < n and self.overlap(current, intervals[i]):
                current = self.merge(current, intervals[i]) 
                i += 1

            res.append(current)

        return res


    def overlap(self, i1, i2):
        return max(i1[0], i1[1]) - min(i2[0], i2[1]) >= 0

    def merge(self, i1, i2):
        i1[0] = min(i1[0], i2[0])
        i1[1] = max(i1[1], i2[1])

        return i1


sol = Solution()
print(sol.insert([[1, 3], [6, 9]], [2, 5]))
print(sol.insert([[1, 2], [3, 5], [6, 7], [8, 10], [12, 16]], [4, 8]))
