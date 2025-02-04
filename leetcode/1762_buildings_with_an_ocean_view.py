from typing import List

class Solution:
    def findBuildings(self, heights: List[int]) -> List[int]:
        """Finds the indices of buildings that have an unobstructed ocean view.
        A building has an ocean view if all the buildings to its right are shorter.

        Args:
            heights (List[int]): A list of integers representing the heights of buildings from left to right.

        Returns:
            List[int]: A list of indices of buildings that have an ocean view, in increasing order."""
        if not heights:
            return []

        max_height = -1
        res = []

        for i in range(len(heights) - 1, -1, -1):
            building = heights[i]
            if building > max_height:
                res.append(i)
                max_height = building

        return list(reversed(res))
