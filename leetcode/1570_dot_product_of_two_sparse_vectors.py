from __future__ import annotations
from typing import List

class SparseVector:

    def __init__(self, nums: List[int]):
        """
        Initializes a sparse vector by storing nonzero elements in a dictionary.

        Args:
            nums (List[int]): The input list representing the sparse vector.
        """
        self.index_to_values_map = {}
        for idx, num in enumerate(nums):
            if num != 0:
                self.index_to_values_map[idx] = num

    def dotProduct(self, vec: SparseVector) -> int:
        """
        Computes the dot product of this sparse vector with another sparse vector.

        Args:
            vec (SparseVector): The other sparse vector.

        Returns:
            int: The dot product result.
        """
        res = 0
        for idx, num in vec.index_to_values_map.items():
            if idx in self.index_to_values_map:
                res += num * self.index_to_values_map[idx]
        return res
