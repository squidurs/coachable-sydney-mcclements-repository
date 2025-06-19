from typing import List

class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        """Computes an array where each element at index `i` is the product
        of all the numbers in the input array except the one at `i`.

        Args:
            nums (List[int]): A list of integers for which the products
                              need to be calculated.

        Returns:
            List[int]: A list where each element is the product of all
                       numbers in the input array except the one at the
                       corresponding index.
        """
        n = len(nums)
        prefix =1
        postfix = 1
        res = [1] * n

        for i in range(n):
            res[i] = prefix
            prefix *= nums[i]

        for i in range(n-1,-1,-1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
