from typing import List
import heapq


# You are given an array of events where events[i] = [startDayi, endDayi].
# Every event i starts at startDayi and ends at endDayi.
#
# You can attend an event i at any day d where startTimei <= d <= endTimei.
# You can only attend one event at any time d.
#
# Return the maximum number of events you can attend.

class Solution:

    def maxEvents(self, events: List[List[int]]) -> int:
        events.sort()
        total_days = max([b for _, b in events])
        event_day = 0
        pq = []

        attended_events = 0
        for day in range(1, total_days + 1):
            while event_day < len(events) and events[event_day][0] == day:
                heapq.heappush(pq, events[event_day][1])
                event_day += 1

            while pq and pq[0] < day:
                heapq.heappop(pq)

            if pq:
                heapq.heappop(pq)
                attended_events += 1

        return attended_events

    def maxEventsGreedy(self, events: List[List[int]]) -> int:
        events = sorted(events, key=lambda x: x[1])

        events_attended = 0
        occupied_days = []

        for event in events:
            for day in range(event[0], event[1] + 1):
                if day not in occupied_days:
                    events_attended += 1
                    occupied_days.append(day)
                    break

        return events_attended


sol = Solution()
print(sol.maxEvents([[1, 2], [2, 3], [3, 4]]))
print(sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 2]]))
print(sol.maxEvents([[1, 2], [1, 2], [3, 3], [1, 5], [1, 5]]))
print(sol.maxEvents([[1, 2], [2, 3], [3, 4], [1, 3]]))
print(sol.maxEvents([[1, 4], [4, 4], [2, 2], [3, 4], [1, 1]]))
