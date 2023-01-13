from typing import List
from heapq import nlargest


# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# rooted at node 0 consisting of n nodes numbered from 0 to n - 1.
# The tree is represented by a 0-indexed array parent of size n,
# where parent[i] is the parent of node i. Since node 0 is the root, parent[0] == -1.
#
# You are also given a string s of length n, where s[i] is the character assigned to node i.
#
# Return the length of the longest path in the tree
# such that no pair of adjacent nodes on the path have the same character assigned to them.

class Solution:
    def longestPath(self, parent: List[int], s: str):  # -> int:
        tree = [[] for _ in range(len(parent))]
        for i, v in enumerate(parent):
            if v >= 0:
                tree[v].append(i)

        ans = 1
        def dsf(node):
            nonlocal ans
            candidate = [0]

            for child in tree[node]:
                current = dsf(child)

                if s[child] != s[node]:
                    candidate.append(current)

            candidate = nlargest(2, candidate)
            ans = max(ans, sum(candidate) + 1) 
            
            return max(candidate) + 1

        dsf(0)

        return ans


sol = Solution()
print(sol.longestPath([-1,0,0,1,1,2], "abacbe")) # INFO: out -> 3
print(sol.longestPath([-1, 0, 0, 0], "aabc")) # INFO: out -> 3
