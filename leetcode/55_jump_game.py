from typing import List

class Solution:
    def canJump(self, nums: List[int]) -> bool:
        """Determines if it's possible to reach the end of the list starting from index 0.

        Args:
            nums (List[int]): A list where each element indicates the max jump length from that index.

        Returns:
            bool: True if the last index is reachable; otherwise, False.
        """
        n = len(nums)
        target = n-1

        for i in range(n-1,-1,-1):
            max_jumps = nums[i]
            if i + max_jumps >= target:
                target = i

        return target == 0
