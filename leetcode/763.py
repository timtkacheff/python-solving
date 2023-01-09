from typing import List


# You are given a string s. We want to partition the string into as many parts as possible
# so that each letter appears in at most one part.
#
# Note that the partition is done so that after concatenating all the parts in order,
# the resultant string should be s.
#
# Return a list of integers representing the size of these parts.

class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        last_appearance = {c: i for i, c in enumerate(s)}
        partitions = []
        
        j = 0
        prev_partition_end = 0
        for i, c in enumerate(s):
            j = max(j, last_appearance[c])

            if i == j:
                partitions.append(i + 1 - prev_partition_end)
                prev_partition_end = i + 1

        return partitions


sol = Solution()
print(sol.partitionLabels('ababcbacadefegdehijhklij'))
print(sol.partitionLabels('eccbbbbdec'))
