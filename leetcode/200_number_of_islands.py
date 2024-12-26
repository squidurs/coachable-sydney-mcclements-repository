from typing import List

class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        """Counts the number of distinct islands in a given grid.

        An island is a group of '1's (land) connected horizontally or vertically.
        The function modifies the input grid to mark visited cells as '0'.

        Args:
            grid (List[List[str]]): A 2D grid where '1' represents land and '0' represents water.

        Returns:
            int: The number of distinct islands in the grid.
        """

        islands = 0
        m = len(grid)
        n = len(grid[0])

        def dfs(r: int, c:int) -> None:
            """Depth-first search to mark all connected land cells as visited.

            Args:
                r (int): Row index of the current cell.
                c (int): Column index of the current cell.
            """
            if r < 0 or r >= m or c < 0 or c >= n or grid[r][c] == '0':
                return
            grid[r][c] = '0'
            directions = [(-1,0), (1,0), (0,1), (0, -1)]
            for dr, dc in directions:
                dfs(r + dr, c+ dc)

        for r in range(m):
            for c in range(n):
                if grid[r][c] == '1':
                    islands += 1
                    dfs(r,c)

        return islands
