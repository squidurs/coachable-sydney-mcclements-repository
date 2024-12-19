class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        """Finds the length of the longest substring without repeating characters.

        Args:
            s (str): Input string to analyze.

        Returns:
            int: The length of the longest substring without repeating characters
        """

        seen = set()
        max_len = 0
        left = 0

        for right in range(len(s)):
            while s[right] in seen:
                seen.remove(s[left])
                left += 1

            cur_len = right - left + 1
            max_len = max(max_len, cur_len)
            seen.add(s[right])

        return max_len
    