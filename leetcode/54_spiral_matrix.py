from typing import List

class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        """_summary_

        Args:
            matrix (List[List[int]]): _description_

        Returns:
            List[int]: _description_
        """

        m, n = len(matrix), len(matrix[0])
        r, c = 0, 0
        UP, DOWN, RIGHT, LEFT = 0, 1, 2, 3
        direction = RIGHT
        ans = []

        UP_WALL = 0
        DOWN_WALL = m
        RIGHT_WALL = n
        LEFT_WALL = -1

        while len(ans) != m*n:
            if direction == RIGHT:
                while c < RIGHT_WALL:
                    ans.append(matrix[r][c])
                    c += 1
                r, c = r + 1, c - 1
                RIGHT_WALL -= 1
                direction = DOWN
            elif direction == DOWN:
                while r < DOWN_WALL:
                    ans.append(matrix[r][c])
                    r += 1
                r, c = r - 1, c - 1
                DOWN_WALL -= 1
                direction = LEFT
            elif direction == LEFT:
                while c > LEFT_WALL:
                    ans.append(matrix[r][c])
                    c -= 1
                r, c = r - 1, c + 1
                LEFT_WALL += 1
                direction = UP
            else:
                while r > UP_WALL:
                    ans.append(matrix[r][c])
                    r -= 1
                r, c = r + 1, c + 1
                UP_WALL += 1
                direction = RIGHT

        return ans

