from typing import Counter, List


# You are given a 0-indexed integer array tasks, 
# where tasks[i] represents the difficulty level of a task. In each round, 
# you can complete either 2 or 3 tasks of the same difficulty level.
#
# Return the minimum rounds required to complete all the tasks, 
# or -1 if it is not possible to complete all the tasks.

class Solution:
    def minimumRounds(self, tasks: List[int]) -> int:
        freq = Counter(tasks)
        steps = 0

        for v in freq.values():
            if v == 1:
                return -1

            if v % 3 == 0:
                steps += v // 3
            else:
                steps += v // 3 + 1

        return steps


sol = Solution()
print(sol.minimumRounds([2, 2, 3, 3, 2, 4, 4, 4, 4, 4]))
print(sol.minimumRounds([2, 3, 3]))
