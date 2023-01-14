from collections import defaultdict


# You are given two strings of the same length s1 and s2 and a string baseStr.
#
# We say s1[i] and s2[i] are equivalent characters.
#
#     For example, if s1 = "abc" and s2 = "cde", then we have 'a' == 'c', 'b' == 'd', and 'c' == 'e'.
#
# Equivalent characters follow the usual rules of any equivalence relation:
#
#     Reflexivity: 'a' == 'a'.
#     Symmetry: 'a' == 'b' implies 'b' == 'a'.
#     Transitivity: 'a' == 'b' and 'b' == 'c' implies 'a' == 'c'.
#
# For example, given the equivalency information from s1 = "abc" and s2 = "cde",
# "acd" and "aab" are equivalent strings of baseStr = "eed",
# and "aab" is the lexicographically smallest equivalent string of baseStr.
#
# Return the lexicographically smallest equivalent string of baseStr by using the equivalency information from s1 and s2.

class Solution:
    # len(s1) = len(s2)
    def smallestEquivalentString(self, s1: str, s2: str, baseStr: str): # -> str:
        graph = defaultdict(set)
        for a, b in zip(s1, s2):
            graph[a].add(b)
            graph[b].add(a)

        def findMin(char, min_char, visited):
            visited.add(char)
            res = min_char

            for node in graph[char]:
                if node not in visited:
                    res = min(res, findMin(node, min(min_char, node), visited))

            return res
        
        res = []
        for ch in baseStr:
            if ch not in graph.keys():
                res.append(ch)
                continue
            
            res.append(findMin(ch, ch, set()))

        return "".join(res)



sol = Solution()
print(sol.smallestEquivalentString("parker", "morris", "parser")) # makkek
print(sol.smallestEquivalentString("hello", "world", "hold")) # hdld
print(sol.smallestEquivalentString("leetcode", "programs", "sourcecode")) # aauaaaaada
