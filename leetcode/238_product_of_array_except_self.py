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
        prefix_list = [1] * n
        postfix_list = [1] * n
        answer = [1] * n

        for i in range(1, n):
            prefix_list[i] = prefix_list[i-1] * nums[i-1]

        for i in range(n-2,-1,-1):
            postfix_list[i] = postfix_list[i+1] * nums[i+1]

        for i in range(n):
            answer[i] = prefix_list[i] * postfix_list[i]

        return answer