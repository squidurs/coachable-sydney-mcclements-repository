from typing import List

class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Rotates an n x n 2D matrix 90 degrees clockwise in-place.

        Args:
            matrix (List[List[int]]): The n x n matrix to be rotated.

        Returns:
            None. The matrix is modified in-place.
        """
        n = len(matrix)

        # Transpose the matrix (swap elements on the diagonal)
        for i in range(n):
            for j in range(i + 1, n):
                matrix[i][j], matrix[j][i] = matrix[j][i], matrix[i][j]

        # Reverse each row
        for i in range(n):
            for j in range(n // 2):
                matrix[i][j], matrix[i][n - j - 1] = matrix[i][n - j - 1], matrix[i][j]
