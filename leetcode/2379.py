import sys


# You are given a 0-indexed string blocks of length n, where blocks[i] is either 'W' or 'B', 
# representing the color of the ith block.
# The characters 'W' and 'B' denote the colors white and black, respectively.
#
# You are also given an integer k, which is the desired number of consecutive black blocks.
#
# In one operation, you can recolor a white block such that it becomes a black block.
#
# Return the minimum number of operations needed such that there
# is at least one occurrence of k consecutive black blocks.

class Solution:
    def minimumRecolors(self, blocks: str, k: int):
        n, flips, count, minOps = len(blocks), 0, 0, sys.maxsize

        i = 0

        for j in range(n):
            if blocks[j] == 'W':
                flips += 1
                count += 1
            elif blocks[j] == 'B':
                count += 1

            if count == k:
                minOps = min(minOps, flips)
                if blocks[i] == 'W':
                    flips -= 1
                    count -= 1
                else:
                    count -= 1
                i += 1

        return minOps


sol = Solution()

print(sol.minimumRecolors("WBWBBBW", 2))
