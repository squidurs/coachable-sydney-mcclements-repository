from collections import defaultdict
from typing import List

class Solution:

    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        """Groups anagram strings by calculating the character frequency of each
        string and using the frequency as a dictionary key to map anagrams together.

        Args:
            strs (List[str]): A list of input strings.

        Returns:
            List[List[str]]: A list of groups, where each group is a list
            of strings that are anagrams of each other.
        """
        anagrams = defaultdict(list)

        for word in strs:

            char_count = [0]*26

            for char in word:
                char_count[ord(char) - ord('a')] += 1

            char_count = ''.join(chr(i + ord('a')) * char_count[i] for i in range(26))

            anagrams[char_count].append(word)

        return list(anagrams.values())
