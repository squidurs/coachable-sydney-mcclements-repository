from typing import List

class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        """Finds the intersections between two lists of intervals.

        Args:
            firstList (List[List[int]]): A list of non-overlapping intervals sorted by start time.
            secondList (List[List[int]]): Another list of non-overlapping intervals sorted by start time.

        Returns:
            List[List[int]]: A list of intersecting intervals between the two input lists.
        """

        i = 0 #pointer for firstList
        j = 0 # pointer for secondList

        intersections = []

        while i < len(firstList) and j < len(secondList):
            a_start, a_end = firstList[i]
            b_start, b_end = secondList[j]

            if b_start <= a_end and a_start <= b_end:
                intersections.append([max(a_start, b_start), min(a_end, b_end)])
            if a_end <= b_end:
                i += 1
            else:
                j += 1

        return intersections
