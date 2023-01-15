from typing import List


# In this problem, a tree is an undirected graph that is connected and has no cycles.
#
# You are given a graph that started as a tree with n nodes labeled from 1 to n,
# with one additional edge added.
# The added edge has two different vertices chosen from 1 to n,
# and was not an edge that already existed.
# The graph is represented as an array edges of length n where edges[i] = [ai, bi]
# indicates that there is an edge between nodes ai and bi in the graph.
#
# Return an edge that can be removed so that the resulting graph is a tree of n nodes.
# If there are multiple answers, return the answer that occurs last in the input.

class Solution:
    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        n = len(edges) + 1
        parent = list(range(n))
        rank = [1] * n

        def find(n):
            if parent[n] != n:
                n = find(parent[n])
            return parent[n]

        def union(n1, n2):
            r1, r2 = find(n1), find(n2)

            if r1 == r2:
                return False

            if rank[r1] > rank[r2]:
                parent[r2] = r1
                rank[r1] += rank[r2]
            else:
                parent[r1] = r2
                rank[r2] += rank[r1]
            return True

        res = []
        for n1, n2 in edges:
            if not union(n1, n2):
                res = [n1, n2]

        return res


sol = Solution()
print(sol.findRedundantConnection([[1, 2], [1, 3], [2, 3]]))  # -> [2, 3]
