from typing import List
import heapq

class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        """Finds the Kth largest element in an unsorted list using a min_heap

        Args:
            nums (List[int]): An unsorted list of integers.
            k (int): The rank of the largest element to find (`k = 1`
                     returns the largest element, `k = 2` the second largest, etc.).

        Returns:
            int: The Kth largest element in the input list.
        """

        min_heap = []

        for num in nums:
            heapq.heappush(min_heap, num)
            if len(min_heap) > k:
                heapq.heappop(min_heap)

        return min_heap[0]
    