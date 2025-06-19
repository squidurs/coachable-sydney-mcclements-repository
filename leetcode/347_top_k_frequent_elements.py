from typing import List
from collections import defaultdict
import heapq

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """
        Finds the k most frequent elements in the input list.

        Uses a hash map to count the frequency of each number,
        then maintains a min-heap of size k to track the top k elements.
        Less frequent elements are popped from the heap as more frequent ones are added.

        Args:
            nums (List[int]): The list of integers.
            k (int): The number of top frequent elements to return.

        Returns:
            List[int]: The k most frequent elements.
        """
        num_count = defaultdict(int)
        heap = []

        for num in nums:
            num_count[num] += 1

        for num, count in num_count.items():
            heapq.heappush(heap, (count, num))
            if len(heap) > k:
                heapq.heappop(heap)

        return [n for _, n in heap]

    def topKFrequent_heap(self, nums: List[int], k: int) -> List[int]:
        """Returns the k most frequent elements from the input list.

        Args:
            nums (List[int]): A list of integers where elements may be repeated.
            k (int): The number of most frequent elements to return.

        Returns:
            List[int]: A list of the k most frequent elements in ascending order
                       of frequency.
        """


        num_count = defaultdict(int)
        heap = []


        for num in nums:
            num_count[num] += 1


        for num, count in num_count.items():
            if len(heap) < k:
                heapq.heappush(heap, (count, num))
            else:
                heapq.heappushpop(heap, (count,num))


        return [h[1] for h in heap]

    def topKFrequent_buckets(self, nums: List[int], k: int) -> List[int]:
        """Returns the k most frequent elements from the input list.
        Frequencies are bucketed by their count (as indices) and the buckets
        are scanned in reverse order to collect the most frequent elements.

        Args:
            nums (List[int]): A list of integers where elements may be repeated.
            k (int): The number of most frequent elements to return.

        Returns:
            List[int]: A list of the k most frequent elements in descending order
                       of frequency.
        """

        num_count = defaultdict(int)

        for num in nums:
            num_count[num] += 1

        n = len(nums)
        buckets = [[] for _ in range(n + 1)]

        for num, count in num_count.items():
            buckets[count].append(num)

        result = []

        for i in range(n, -1, -1):
            for num in buckets[i]:
                result.append(num)
                if len(result) == k:
                    return result
