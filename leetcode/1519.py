from typing import Counter, List

# You are given a tree (i.e. a connected, undirected graph that has no cycles)
# consisting of n nodes numbered from 0 to n - 1 and exactly n - 1 edges.
# The root of the tree is the node 0,
# and each node of the tree has a label which is a lower-case character given in the string labels
# (i.e. The node with the number i has the label labels[i]).
#
# The edges array is given on the form edges[i] = [ai, bi],
# which means there is an edge between nodes ai and bi in the tree.
#
# Return an array of size n where ans[i] is the number of nodes in the subtree
# of the ith node which have the same label as node i.
#
# A subtree of a tree T is the tree consisting of a node in T and all of its descendant nodes.

class Solution:
    def countSubTrees(self, n: int, edges: List[List[int]], labels: str) -> List[int]:
        res = [0] * n

        adj = [[] for _ in range(n)] 
        for a, b in edges:
            adj[a].append(b)
            adj[b].append(a)

        visited = set()
        def traverse(node):
            nonlocal res
            count = Counter()

            if node in visited:
                return count
            visited.add(node)

            for adjacent in adj[node]:
                count += traverse(adjacent)

            count[labels[node]] += 1
            res[node] = count[labels[node]]

            return count
        
        traverse(0)
        return res


sol = Solution()
print(sol.countSubTrees(7, [[0, 1], [0, 2], [1, 4], [1, 5], [2, 3], [2, 6]], "abaedcd"))
