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
        prefixSums = {0:1}
        count = 0
        cur_sum = 0

        for i in range(len(nums)):
            cur_sum += nums[i]

            if cur_sum - k in prefixSums:
                count += prefixSums[cur_sum - k]

            if cur_sum in prefixSums:
                prefixSums[cur_sum] += 1
            else:
                prefixSums[cur_sum] = 1

        return count
