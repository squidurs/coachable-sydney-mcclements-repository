from typing import List

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        """Finds the maximum number of consecutive 1's in the binary array `nums`
        if you are allowed to flip at most `k` 0's to 1's.

        Args:
            nums (List[int]): A list of binary integers (0s and 1s).
            k (int): The maximum number of 0's that can be flipped to 1's.

        Returns:
            int: The maximum number of consecutive 1's after flipping at most `k` 0's.
        """

        n = len(nums)
        max_ones = 0
        num_zeros = 0
        left = 0

        for right in range(n):
            if nums[right] == 0:
                num_zeros += 1

            while num_zeros > k:
                if nums[left] == 0:
                    num_zeros -= 1
                left += 1

            window_size = right - left + 1
            max_ones = max(max_ones, window_size)

        return max_ones
