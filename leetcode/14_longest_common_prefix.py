from typing import List

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string among an array of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. Returns an empty string if there is none.
        """
        res = []

        for chars in zip(*strs):
            if len(set(chars)) != 1:
                break
            else:
                res.append(chars[0])

        return ''.join(res)

    def longestCommonPrefix2(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string among an array of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. Returns an empty string if there is none.
        """
        if not strs:
            return ""

        for i in range(len(strs[0])):
            char = strs[0][i]
            for s in strs[1:]:
                if i == len(s) or s[i] != char:
                    return strs[0][:i]
        return strs[0]

    def longestCommonPrefix3(self, strs: List[str]) -> str:
        """
        Finds the longest common prefix string among an array of strings.

        Args:
            strs (List[str]): A list of strings.

        Returns:
            str: The longest common prefix. Returns an empty string if there is none.
        """
        if not strs:
            return ""

        prefix = strs[0]
        for s in strs[1:]:
            while not s.startswith(prefix):
                prefix = prefix[:-1]
                if not prefix:
                    return ""
        return prefix