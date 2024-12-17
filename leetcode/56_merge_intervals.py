from typing import List

class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        """Merges overlapping intervals in a given list.

        Args:
            intervals (List[List[int]]): A list of intervals represented as [start, end].

        Returns:
            List[List[int]]: A list of merged intervals where all overlapping intervals
                             have been combined into a single interval.
        """

        intervals.sort(key = lambda i : i[0])

        result = [intervals[0]]

        for start, end in intervals:
            lastEnd = result[-1][1]
            if start <= lastEnd:
                result[-1][1] = max(lastEnd, end)
            else:
                result.append([start, end])

        return result
