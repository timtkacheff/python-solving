from typing import List

# Given two n x n binary matrices mat and target,
# return true if it is possible to make mat equal to target
# by rotating mat in 90-degree increments,
# or false otherwise.


class Solution:
    def findRotation(self, mat: List[List[int]],
                     target: List[List[int]]) -> bool:
        for _ in range(4):
            if mat == target:
                return True
            mat = [list(x) for x in zip(*mat[::-1])]

        return False


sol = Solution()
mat = [[0, 1], [1, 0]]
target = [[1, 0], [0, 1]]

print(sol.findRotation(mat, target))
