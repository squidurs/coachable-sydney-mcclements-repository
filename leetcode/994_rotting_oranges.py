from collections import deque
from typing import List

class Solution:
    def orangesRotting(self, grid: List[List[int]]) -> int:
        """Determines the minimum time required for all fresh oranges in a grid to rot.
        Rotting oranges spread to adjacent fresh oranges every minute. If there are
        unreachable fresh oranges, the function returns -1.

        Args:
            grid (List[List[int]]): A 2D grid where:
                - 0 represents an empty cell
                - 1 represents a fresh orange
                - 2 represents a rotten orange

        Returns:
            int: The number of minutes required for all fresh oranges to rot, or -1
            if it is impossible for all fresh oranges to rot.
        """

        fresh = 0
        q = deque()
        m = len(grid)
        n = len(grid[0])

        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i, j))
                elif grid[i][j] == 1:
                    fresh += 1

        if fresh == 0:
            return 0

        minutes = 0
        while q:
            q_size = len(q)
            minutes += 1
            for _ in range(q_size):
                i, j = q.popleft()
                for r, c in [(i, j+1), (i+1, j), (i-1, j), (i, j-1)]:
                    if 0 <= r < m and 0 <= c < n and grid[r][c] == 1:
                        grid[r][c] = 2
                        fresh -= 1
                        q.append((r,c))

        if fresh == 0:
            return minutes - 1
        else:
            return -1
