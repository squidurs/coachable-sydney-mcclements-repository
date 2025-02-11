import math
import heapq
from random import randint
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


    def kClosest_qs(self, points: List[List[int]], k: int) -> List[List[int]]:
        """
        Finds the k closest points to the origin (0,0) using quickselect

        Args:
            points (List[List[int]]): A list of points represented as [x, y].
            k (int): The number of closest points to return.

        Returns:
            List[List[int]]: The k closest points to the origin.
        """

        def distance(point: List[int]) -> int:
            """
            Calculates the distance from the origin.

            Args:
                point (List[int]): A point represented as [x, y].

            Returns:
                int: The distance from 'point' to the origin.
            """
            return point[0]**2 + point[1]**2

        def quickselect(left: int, right: int, k: int):
            """
            Partitions the points so that the k closest points are in the first k positions.

            Args:
                left (int): Left boundary of the current partition.
                right (int): Right boundary of the current partition.
                k (int): The number of closest points to identify.
            """
            if left >= right:
                return

            pivot_idx = randint(left, right)
            pivot_distance = distance(points[pivot_idx])

            points[pivot_idx], points[right] = points[right], points[pivot_idx]

            i = left
            for j in range(left, right):
                if distance(points[j]) <= pivot_distance:
                    points[i], points[j] = points[j], points[i]
                    i += 1

            points[i], points[right] = points[right], points[i]

            if i == k:
                return
            elif i < k:
                quickselect(i + 1, right, k)
            else:
                quickselect(left, i - 1, k)

        quickselect(0, len(points) - 1, k)
        return points[:k]
