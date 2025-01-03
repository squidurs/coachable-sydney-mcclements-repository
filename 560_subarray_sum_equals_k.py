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
        curSum = 0

        for i in range(len(nums)):
            curSum += nums[i]

            if curSum - k in prefixSums:
                count += prefixSums[curSum - k]

            if curSum in prefixSums:
                prefixSums[curSum] += 1
            else:
                prefixSums[curSum] = 1

        return count
