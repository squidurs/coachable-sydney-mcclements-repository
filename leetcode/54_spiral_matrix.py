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

        ans = []

        UP_WALL = 0
        DOWN_WALL = m - 1
        RIGHT_WALL = n - 1
        LEFT_WALL = 0

        def in_bounds(next_r, next_c):
            """
            checks if the next cell will be in bounds.
            """
            return UP_WALL <= next_r <= DOWN_WALL and LEFT_WALL <= next_c <= RIGHT_WALL

        while len(ans) != m*n:
            ans.append(matrix[r][c])

            dr, dc = DIRECTIONS[cur_dir]
            next_r, next_c = r + dr, c + dc

            if not in_bounds(next_r, next_c):
                if cur_dir == 0: #right
                    UP_WALL += 1
                elif cur_dir == 1: #down
                    RIGHT_WALL -= 1
                elif cur_dir == 2: #left
                    DOWN_WALL -= 1
                elif cur_dir == 3: #up
                    LEFT_WALL += 1

                cur_dir = (cur_dir + 1) % 4
                dr, dc = DIRECTIONS[cur_dir]
                next_r, next_c = r + dr, c + dc

            r, c = next_r, next_c

        return ans


