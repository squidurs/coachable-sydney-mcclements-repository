from typing import List

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        """Concatenates the input list with itself.

        Args:
            nums (List[int]): A list of integers.

        Returns:
            List[int]: A new list consisting of two copies of the input list.
        """
        return nums + nums