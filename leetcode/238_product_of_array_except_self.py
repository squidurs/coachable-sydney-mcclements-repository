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
        prefix_product = 1
        postfix_product = 1
        answer = [0]*n
        for i in range(n):
            answer[i] = prefix_product
            prefix_product *= nums[i]
        for i in range(n-1,-1,-1):
            answer[i] *= postfix_product
            postfix_product *= nums[i]
        return answer