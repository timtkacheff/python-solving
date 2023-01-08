from typing import List
from collections import defaultdict
from math import atan2


# Given an array of points where points[i] = [xi, yi] represents a point on the X-Y plane,
# return the maximum number of points that lie on the same straight line.

class Solution:
    def maxPoints(self, points: List[List[int]]) -> int:
        n = len(points)
        if n == 1:
            return 1

        result = 0
        for i in range(n):
            cnt = defaultdict(int)
            for j in range(n):
                # Exclude the same point
                if j != i:
                    # Calculate acrtangent of vector with coordinates {x1, y1}, {x2, y2}
                    cnt[atan2(points[j][1] - points[i][1],
                              points[j][0] - points[i][0])] += 1
            
            # Add 1 to max(cnt.values()) to add points[i]
            result = max(result, max(cnt.values()) + 1)

        return result


sol = Solution()
print(sol.maxPoints([[1, 1], [2, 2], [3, 3]]))
print(sol.maxPoints([[1, 1], [3, 2], [5, 3], [4, 1], [2, 3], [1, 4]]))
