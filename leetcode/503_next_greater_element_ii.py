from typing import List

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        """Finds the next greater element for each element in a circular array.

        Args:
            nums (List[int]): A list of integers representing the circular array.

        Returns:
            List[int]: A list where each element represents the next greater element
                       for the corresponding index in the input list, or -1 if no
                       greater element exists.
        """

        n = len(nums)
        result = [-1]*n
        stack = []

        for i in range(2*n):
            cur_idx = i % n
            while stack and nums[cur_idx] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[cur_idx]

            if i < n:
                stack.append(cur_idx)

        return result
