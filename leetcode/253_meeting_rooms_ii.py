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
        min_end_times = [intervals[0][1]]

        for start, end in intervals[1:]:
            if start >= min_end_times[0]:
                heapq.heappop(min_end_times)
            heapq.heappush(min_end_times, end)

        return len(min_end_times)
    