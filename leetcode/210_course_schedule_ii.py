from collections import defaultdict
from typing import List

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        """
        Determines the order in which courses should be taken to satisfy all prerequisites.

        Args:
            numCourses (int): The total number of courses labeled from 0 to numCourses - 1.
            prerequisites (List[List[int]]): A list of prerequisite pairs where each pair [a, b]
            means course `b` is a prerequisite for course `a`.

        Returns:
            List[int]: A list of courses in the order they should be taken. If it is impossible
            to complete all courses (due to a cycle), returns an empty list.
        """

        order = []
        adj_list = defaultdict(list)
        for source, target in prerequisites:
            adj_list[source].append(target)

        UNVISITED, VISITING, VISITED = 0, 1, 2
        status = [UNVISITED] * numCourses

        def dfs(i: int) -> bool:
            """Performs a depth-first search to determine if the course can be completed.

            Checks for cycles in the graph and adds the course to the `order`
            list if all its prerequisites have been successfully visited.

            Args:
                i (int): The course index to process.

            Returns:
                bool: `True` if the course and all its prerequisites can be successfully completed;
                `False` if a cycle is detected.
            """
            if status[i] == VISITING:
                return False
            if status[i] == VISITED:
                return True
            status[i] = VISITING

            for prereq in adj_list[i]:
                if not dfs(prereq):
                    return False

            status[i] = VISITED
            order.append(i)
            return True

        for i in range(numCourses):
            if not dfs(i):
                return []

        return order
