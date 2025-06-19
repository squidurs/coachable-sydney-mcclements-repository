from typing import List

class NumMatrix:

    def __init__(self, matrix: List[List[int]]):
        """
        Initializes the NumMatrix object with a 2D prefix sum array.
        The prefix array stores cumulative sums from (0,0) to (i,j) for O(1) queries.
        """
        self.matrix = matrix
        row, col = len(matrix), len(matrix[0])
        self.prefix = [[0] * (col + 1) for _ in range(row + 1)]

        for r in range(row):
            for c in range(col):
                self.prefix[r+1][c+1] = matrix[r][c] + self.prefix[r+1][c] + self.prefix[r][c+1] - self.prefix[r][c]


    def sumRegion(self, row1: int, col1: int, row2: int, col2: int) -> int:
        """
        Returns the sum of elements inside the rectangle
        defined by (row1, col1) to (row2, col2), inclusive.
        """
        return (self.prefix[row2 + 1][col2 + 1] - self.prefix[row1][col2 + 1] - self.prefix[row2 + 1][col1] + self.prefix[row1][col1])



# Your NumMatrix object will be instantiated and called as such:
# obj = NumMatrix(matrix)
# param_1 = obj.sumRegion(row1,col1,row2,col2)