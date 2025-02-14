# TEST CASES

# 1. Row win
# Board size: 3x3
#  1  1 (1)
# -1 -1  _
#  _  _  _
# move(0, 2, 1) → Expected output: 1 (Player 1 wins)

# 2. Column win
#  1  -1  _
#  1  -1  _
#  _ (-1) _
# move(2, 1, 2) → Expected output: 2 (Player 2 wins)

# 3. Win in the main diagonal
#  1 -1  _
# -1  1  _
#  _  _ (1)
# move(2, 2, 1) → Expected output: 1 (Player 1 wins)

# 4. Win in the anti-diagonal
#   1 -1 -1
#  -1 -1  _
# (-1) _  1
# move(2, 0, 2) → Expected output: 2 (Player 2 wins)

# 5. No winner
#  1 -1  1
# -1  _ -1
# -1  1 (1)
# move(2, 2, 1) → Expected output: 0 (no winner)

class TicTacToe:
    """
    A class to implement a Tic-Tac-Toe game.

    Attributes:
        n (int): The size of the board (n x n).
        row_totals (list[int]): Tracks the sum of each row.
        col_totals (list[int]): Tracks the sum of each column.
        diagonal (int): Sum of the main diagonal.
        anti_diagonal (int): Sum of the anti-diagonal.
    """
    def __init__(self, n: int):
        """
        Initialize the board with size n x n.
        """
        self.n = n
        self.row_totals = [0] * n
        self.col_totals = [0] * n
        self.diagonal = 0
        self.anti_diagonal = 0

    def move(self, row: int, col: int, player: int) -> int:
        """
        Makes a move for a given player at (row, col).

        Args:
            row (int): Row index of the move.
            col (int): Column index of the move.
            player (int): The player making the move (1 or 2).

        Returns:
            int: 0 if no winner yet, or the winning player's number (1 or 2).
        """
        mark = 1 if player == 1 else -1  # Player 1 -> +1, Player 2 -> -1

        self.row_totals[row] += mark
        self.col_totals[col] += mark

        if row == col:
            self.diagonal += mark
        if row + col == self.n - 1:
            self.anti_diagonal += mark

        if max(abs(self.row_totals[row]),
               abs(self.col_totals[col]),
               abs(self.diagonal),
               abs(self.anti_diagonal)) == self.n:
            return player
        return 0
