from typing import List
import heapq
import random

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

    def quickselect_KthLargest(self, nums: List[int], k: int) -> int:
        """Finds the Kth largest element in an unsorted list using quickselect

        Args:
            nums (List[int]): An unsorted list of integers.
            k (int): The rank of the largest element to find (`k = 1`
                     returns the largest element, `k = 2` the second largest, etc.).

        Returns:
            int: The Kth largest element in the input list.
        """
        def partition(low, high):

            pivot_idx = random.randint(low, high)
            pivot_value = nums[pivot_idx]

            nums[pivot_idx], nums[high] = nums[high], nums[pivot_idx]

            store_idx = low
            for i in range(low, high):
                if nums[i] > pivot_value:
                    nums[store_idx], nums[i] = nums[i], nums[store_idx]
                    store_idx += 1

            nums[high], nums[store_idx] = nums[store_idx], nums[high]
            return store_idx

        def quickselect(low, high, k_largest):
            if low == high:
                return nums[low]

            pivot_idx = partition(low, high)

            if pivot_idx == k_largest:
                return nums[pivot_idx]

            elif pivot_idx > k_largest:
                return quickselect(low, pivot_idx - 1, k_largest)

            else:
                return quickselect(pivot_idx + 1, high, k_largest)

        return quickselect(0, len(nums)-1, k-1)

