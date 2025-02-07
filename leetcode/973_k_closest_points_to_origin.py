import math
import heapq
from typing import List

class Solution:
    def kClosest(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0,0) from a list of points.

        Args:
            points (List[List[int]]): A list of points where each point is represented as [x, y].
            k (int): The number of closest points to return.

        Returns:
            List[List[int]]: A list containing the k closest points to the origin.
        """
        max_heap = []

        for x, y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(max_heap, (-distance, [x,y]))
            if len(max_heap) > k:
                heapq.heappop(max_heap)

        return [point for _, point in max_heap]
