from typing import List

# There are some spherical balloons taped onto a flat wall that represents the XY-plane.
# The balloons are represented as a 2D integer array points where points[i] = [xstart, xend]
# denotes a balloon whose horizontal diameter stretches between xstart and xend.
# You do not know the exact y-coordinates of the balloons.
#
# Arrows can be shot up directly vertically (in the positive y-direction) from different points along the x-axis.
# A balloon with xstart and xend is burst by an arrow shot at x if xstart <= x <= xend.
# There is no limit to the number of arrows that can be shot.
# A shot arrow keeps traveling up infinitely, bursting any balloons in its path.
#
# Given the array points, return the minimum number of arrows that must be shot to burst all balloons.


class Solution:
    def findMinArrowShots(self, points: List[List[int]]):  # -> int:
        points = sorted(points, key=lambda x: x[1])
        res, min = 0, -float('inf')
        for interval in points:
            if interval[0] > min:
                res += 1
                min = interval[1]

        return res


sol = Solution()
print(sol.findMinArrowShots([[10, 16], [2, 8], [1, 6], [7, 12]]))
print(sol.findMinArrowShots(
    [[10, 16], [2, 8], [1, 6], [7, 12], [7, 12], [7, 12]]))
print(sol.findMinArrowShots([[1, 2], [1, 2], [3, 4], [5, 6], [7, 8]]))
