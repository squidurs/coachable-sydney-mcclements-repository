from typing import List
import heapq

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        """Calculates the minimum number of meeting rooms required to accommodate all meetings.

        Args:
            intervals (List[List[int]]): A list of meeting intervals, where each interval is
                                         represented as [start, end].

        Returns:
            int: The minimum number of meeting rooms required.
        """

        #sort by meeting start time
        intervals.sort()
        #min-heap to track end times of meetings currently occupying rooms
        meeting_rooms_heap = [intervals[0][1]]

        for start, end in intervals[1:]:
            if start >= meeting_rooms_heap[0]:
                heapq.heappop(meeting_rooms_heap)
            heapq.heappush(meeting_rooms_heap, end)

        return len(meeting_rooms_heap)


