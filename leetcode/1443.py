from typing import List


# Given an undirected tree consisting of n vertices numbered from 0 to n-1,
# which has some apples in their vertices. You spend 1 second to walk over one edge of the tree.
# Return the minimum time in seconds you have to spend to collect all apples in the tree,
# starting at vertex 0 and coming back to this vertex.
#
# The edges of the undirected tree are given in the array edges,
# where edges[i] = [ai, bi] means that exists an edge connecting the vertices ai and bi.
# Additionally, there is a boolean array hasApple,
# where hasApple[i] = true means that vertex i has an apple; otherwise, it does not have any apple.

class Solution:
    def minTime(self, n: int, edges: List[List[int]], hasApple: List[bool]) -> int:
        adjacency = [[] for _ in range(n)]
        for i, j in edges:
            adjacency[i].append(j)
            adjacency[j].append(i)

        visited = set()

        def dsf(node) -> int:
            if node in visited:
                return 0
            visited.add(node)

            secs = 0
            for adjacent in adjacency[node]:
                secs += dsf(adjacent)

            if secs > 0:
                return secs + 2

            return 2 if hasApple[node] else 0

        return max(dsf(0) - 2, 0)


sol = Solution()
print(sol.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [
      False, False, True, False, True, True, False]))
print(sol.minTime(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], [
      False, False, False, False, False, False, False]))
