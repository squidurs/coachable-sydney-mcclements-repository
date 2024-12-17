from typing import List
from collections import defaultdict

class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        """Returns the k most frequent elements from the input list.

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
        buckets = [0] * (n+1)

        for num, count in num_count.items():
            if buckets[count] == 0:
                buckets[count] = [num]
            else:
                buckets[count].append(num)

        result = []

        for i in range(n, -1, -1):
            if buckets[i] != 0:
                result.extend(buckets[i])
            if len(result) == k:
                break

        return result
