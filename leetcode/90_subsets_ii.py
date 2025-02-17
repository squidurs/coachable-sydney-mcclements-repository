from typing import List

class Solution:

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Generates all unique subsets of a list of integers, including handling duplicates.

        Args:
            nums (List[int]): A list of integers, which may contain duplicates.

        Returns:
            List[List[int]]: A list of unique subsets of the input list.
        """

        res = []

        def backtrack(i: int, subset: List[int]) -> None:
            """Recursively generates subsets by including or excluding each element.

            Args:
                i (int): The current index in the list to process.
                subset (List[int]): The current subset being built.
            """
            if i == len(nums):
                res.append(tuple(subset))  # store subsets as tuples for deduplication
                return

            # Include nums[i]
            backtrack(i + 1, subset + [nums[i]])

            # Exclude nums[i]
            backtrack(i + 1, subset)

        backtrack(0, [])

        unique_subsets = set(res) # Remove duplicates by converting to a set
        # Convert the set of tuples back into a list of lists
        result = [list(subset) for subset in unique_subsets]

        return result


    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible subsets of a list of integers, ensuring no duplicate subsets.

        Args:
            nums (List[int]): A list of integers, possibly containing duplicates.

        Returns:
            List[List[int]]: A list of all unique subsets.
        """

        nums.sort()
        res = [[]]
        prev_end = 0

        for i in range(len(nums)):
            start = 0

            if i > 0 and nums[i] == nums[i - 1]:
                start = prev_end

            prev_end = len(res)

            for j in range(start, len(res)):
                res.append(res[j] + [nums[i]])

        return res

    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        """Generates all possible subsets of a list of integers with backtracking, ensuring no duplicates.

        Args:
            nums (List[int]): A list of integers, possibly containing duplicates.

        Returns:
            List[List[int]]: A list of all unique subsets.
        """
        res = []
        nums.sort()

        def backtrack(i: int, subset: List[int]) -> None:
            """Helper function for backtracking to find all unique subsets.

            Args:
                i (int): Current index in the list of numbers.
                subset (List[int]): The current subset being built.
            """

            if i == len(nums):
                res.append(subset[::])
                return
            # include current element and recurse with the next element
            subset.append(nums[i])
            backtrack(i+1, subset)
            subset.pop() # Backtrack: remove the element added to subset and explore excluding it.

            #skip duplicate elements
            while i + 1 < len(nums) and nums[i + 1] == nums[i]:
                i += 1
            backtrack(i+1, subset)

        backtrack(0, [])
        return res
