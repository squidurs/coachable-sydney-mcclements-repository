from collections import Counter

class Solution:
    def minimumPushes(self, word: str) -> int:
        """Calculates the minimum number of button presses needed to form a word
        on a remapped keypad with 8 available positions.

        Args:
            word (str): The word to be typed.

        Returns:
            int: The total number of button presses required.
        """

        char_count = Counter(word)

        frequencies = sorted(char_count.values(), reverse=True)
        total_pushes = 0

        for i, freq in enumerate(frequencies):
            group = (i // 8) + 1
            total_pushes += group * freq

        return total_pushes
