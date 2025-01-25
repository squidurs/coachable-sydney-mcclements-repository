from typing import List

class Solution:
    def minHeightShelves(self, books: List[List[int]], shelfWidth: int) -> int:
        """Calculates the minimum height of a bookshelf needed to arrange books in order.

        Args:
            books (List[List[int]]): A list of books, where each book is represented as [width, height].
            shelfWidth (int): The maximum width of each shelf.

        Returns:
            int: The minimum height of the bookshelf to accommodate all books.
        """

        n = len(books)
        dp = [float('inf')] * (n+1)
        dp[0] = 0

        for i in range(1, n + 1):
            width = 0
            max_height = 0

            # For each book 'i', find the optimal total height by considering all valid
            # groupings of books 'i-j' on the same shelf
            for j in range(i, 0, -1):
                book_width, book_height = books[j-1]
                width += book_width
                max_height = max(max_height, book_height)

                if width > shelfWidth:
                    break

                dp[i] = min(dp[i], dp[j-1] + max_height)

        return dp[n]
