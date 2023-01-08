from typing import List


# There are n flights that are labeled from 1 to n.
#
# You are given an array of flight bookings bookings,
# where bookings[i] = [firsti, lasti, seatsi] represents a booking for flights
# first[i] through last[i] (inclusive) with seatsi seats reserved for each flight in the range.
#
# Return an array answer of length n, where answer[i] is the total number of seats reserved for flight i.

class Solution:
    # -> List[int]:
    def corpFlightBookings(self, bookings: List[List[int]], n: int):
        reserved_seats = [0] * (n+1)

        for booking in bookings:
            reserved_seats[booking[0] - 1] += booking[2]
            reserved_seats[booking[1]] -= booking[2]

        tmp = 0
        for i in range(n):
            tmp += reserved_seats[i]
            reserved_seats[i] = tmp

        return reserved_seats[:n]


sol = Solution()
print(sol.corpFlightBookings([[1, 2, 10], [2, 3, 20], [2, 5, 25]], 5))
