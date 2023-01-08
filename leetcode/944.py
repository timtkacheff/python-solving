from typing import List


# You are given an array of n strings strs, all of the same length.
#
# The strings can be arranged such that there is one on each line, making a grid.
# For example, strs = ["abc", "bce", "cae"] can be arranged as:
#
#     abc
#     bce
#     cae
#
# You want to delete the columns that are not sorted lexicographically. 
# In the above example (0-indexed), columns 0 ('a', 'b', 'c') and 2 ('c', 'e', 'e')
# are sorted while column 1 ('b', 'c', 'a') is not, so you would delete column 1.
#
# Return the number of columns that you will delete.

class Solution:
    def minDeletionSize(self, strs: List[str]) -> int:
        res = 0 
        for v in zip(*strs):
            if list(v) != sorted(v):
                res += 1

        return res


sol = Solution()
print(sol.minDeletionSize(["cba", "daf", "ghi"]))
