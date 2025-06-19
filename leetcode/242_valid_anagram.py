from collections import defaultdict

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        """
        Checks if two strings are anagrams of each other.

        Args:
            s (str): First string.
            t (str): Second string.

        Returns:
            bool: True if t and s are anagrams, False otherwise.
        """
        if len(s) != len(t):
            return False

        char_count = defaultdict(int)

        for char in s:
            char_count[char] += 1

        for char in t:
            char_count[char] -= 1

        for count in char_count.values():
            if count != 0:
                return False

        return True