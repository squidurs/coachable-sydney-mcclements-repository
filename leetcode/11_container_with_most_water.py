from typing import List

class Solution:
    def maxArea(self, height: List[int]) -> int:
        """Finds the maximum area of water a container can hold,
        where the width of the container is the distance between two lines
        and the height is the shorter of the two lines.

        Args:
            height (List[int]): A list of integers where each value represents the height of a vertical line.

        Returns:
            int: The maximum area of water that can be contained.
        """

        n = len(height)
        left = 0
        right = n - 1
        max_area = 0

        while left < right:
            area = min(height[left], height[right]) * (right - left)
            max_area = max(max_area, area)

            if height[left] < height[right]:
                left += 1

            else:
                right -= 1

        return max_area