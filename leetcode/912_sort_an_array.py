from typing import List
import random

class Solution:
    def sortArray(self, nums: List[int]) -> List[int]:
        """
        Sorts an array using QuickSort with 3-way partitioning for improved performance
        on arrays with many duplicate elements.

        Args:
            nums (List[int]): The list of integers to sort.

        Returns:
            List[int]: The sorted list.
        """
        def three_way_partition(lo, hi):
            """
            Partitions the subarray nums[lo:hi+1] into three parts:
            - Elements less than the pivot
            - Elements equal to the pivot
            - Elements greater than the pivot

            Returns:
                (int, int): Indices marking the boundaries of elements equal to the pivot.
            """
            pivot_idx = random.randint(lo, hi)
            pivot = nums[pivot_idx]
            nums[lo], nums[pivot_idx] = nums[pivot_idx], nums[lo]

            lt = lo    # nums[lo:lt] < pivot
            gt = hi    # nums[gt+1:hi+1] > pivot
            i = lo + 1 # nums[lt:i] == pivot

            while i <= gt:
                if nums[i] < pivot:
                    nums[i], nums[lt] = nums[lt], nums[i]
                    lt += 1
                    i += 1
                elif nums[i] > pivot:
                    nums[i], nums[gt] = nums[gt], nums[i]
                    gt -= 1
                else:
                    i += 1
            return lt, gt

        def quicksort(lo, hi):
            """
            Recursively sorts the subarray nums[lo:hi+1] using 3-way partitioning.
            """
            if lo < hi:
                lt, gt = three_way_partition(lo, hi)
                quicksort(lo, lt - 1)
                quicksort(gt + 1, hi)

        quicksort(0, len(nums) - 1)
        return nums
