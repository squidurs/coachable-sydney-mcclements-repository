from typing import List

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        """
        Finds the total number of subarrays whose sum equals k

        Args:
            nums (List[int]): List of integers.
            k (int): The target sum for subarrays.

        Returns:
            int: The count of subarrays whose sum equals k
        """
        prefix_sum_counts = {0:1}
        cur_sum = 0
        count = 0

        for num in nums:
            cur_sum += num
            if cur_sum - k in prefix_sum_counts:
                count += prefix_sum_counts[cur_sum - k]
            if cur_sum in prefix_sum_counts:
                prefix_sum_counts[cur_sum] += 1
            else:
                prefix_sum_counts[cur_sum] = 1

        return count
