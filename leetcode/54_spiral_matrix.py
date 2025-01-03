from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """Returns the elements of the given 2D matrix in spiral order.

        Args:
            matrix (List[List[int]]): A 2D list representing the input matrix.

        Returns:
            List[int]: A list of integers representing the matrix elements in spiral order.
        """

        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        UP = (-1,0)
        DOWN = (1,0)
        LEFT = (0,-1)
        RIGHT = (0,1)
        DIRECTIONS = [RIGHT, DOWN, LEFT, UP]
        cur_dir = 0
        visited = set()
        ans = []

        def in_bounds_unvisited(row, col):
            """
            checks if the cell is in bounds and is not visited.
            """
            return 0 <= row < m and 0 <= col < n and (row, col) not in visited


        while len(ans) != m*n:
            ans.append(matrix[r][c])
            visited.add((r, c))

            dr, dc = DIRECTIONS[cur_dir]
            next_r, next_c = r + dr, c + dc

            if not in_bounds_unvisited(next_r, next_c):
                cur_dir = (cur_dir + 1) % 4
                dr, dc = DIRECTIONS[cur_dir]
                next_r, next_c = r + dr, c + dc

            r, c = next_r, next_c

        return ans


