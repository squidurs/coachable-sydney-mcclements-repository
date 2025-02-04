from typing import List
from collections import deque

class Solution:
    def shortestPathBinaryMatrix(self, grid: List[List[int]]) -> int:
        """Uses BFS to find the shortest clear path from the top-left to the bottom-right corner in a binary matrix,
        where only 0s are traversable.

        Args:
            grid (List[List[int]]): A binary matrix where 0 represents a walkable cell and 1 represents an obstacle.

        Returns:
            int: The shortest path length, or -1 if no path exists.
        """
        n = len(grid)

        if grid[0][0] == 1 or grid[n-1][n-1] == 1:
            return -1

        directions = [(-1,-1), (-1,0), (-1,1), (0,-1), (0,1), (1,-1), (1,0), (1,1)]
        visited = set()
        visited.add((0,0))
        queue = deque([(0,0,1)])

        while queue:
            row, col, path_len = queue.popleft()
            if (row, col) == (n-1, n-1):
                return path_len
            for dr, dc in directions:
                nr, nc = row + dr, col + dc
                if 0 <= nr < n and 0 <= nc < n and (nr,nc) not in visited and grid[nr][nc] == 0:
                    queue.append((nr, nc, path_len + 1))
                    visited.add((nr,nc))
        return -1
