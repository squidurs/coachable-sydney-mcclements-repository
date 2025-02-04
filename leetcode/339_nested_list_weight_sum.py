from typing import List
from collections import deque
from __future__ import annotations

# Dummy implementation to avoid errors in local IDE
class NestedInteger:
    def isInteger(self) -> bool:
        """Return True if this NestedInteger holds a single integer, otherwise False."""
        pass

    def getInteger(self) -> int:
        """Return the single integer that this NestedInteger holds, or None if it holds a nested list."""
        pass

    def getList(self) -> List[NestedInteger]:
        """Return the nested list that this NestedInteger holds, or None if it holds a single integer."""
        pass

class Solution:
    def depthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        Calculates the weighted sum of integers in a nested list based on their depth.

        Args:
            nestedList (List[NestedInteger]): The nested list of integers and lists.

        Returns:
            int: The weighted sum of integers.
        """
        res = 0
        queue = deque([(el, 1) for el in nestedList])  # Add depth info as part of the tuple

        while queue:
            cur, depth = queue.popleft()
            if cur.isInteger():
                res += cur.getInteger() * depth
            else:
                for nested in cur.getList():
                    queue.append((nested, depth + 1))  # Increment depth for nested elements

        return res

    def dfsDepthSum(self, nestedList: List[NestedInteger]) -> int:
        """
        Computes the depth-weighted sum of all integers in the nested list.

        Args:
            nestedList (List[NestedInteger]): The nested list.

        Returns:
            int: The total weighted sum.
        """
        def dfs(nested_list: List[NestedInteger], depth) -> int:
            """Recursively computes the depth-weighted sum of all integers in a nested list.

            The 'res' for a given level is the sum of the totals from its children (sub-lists or integers),
            where each integer is multiplied by its depth.

            Args:
                nested_list (List[NestedInteger]): The current level of the nested list.
                depth (int): The depth of the current level in the nested list.

            Returns:
                int: The total weighted sum of all integers at this level and deeper.
        """
            res = 0
            for el in nested_list:
                if el.isInteger():
                    res += el.getInteger() * depth
                else:
                    res += dfs(el.getList(), depth + 1) # Recur for the inner list with increased depth
            return res

        return dfs(nestedList, 1)


    def depthSum2(self, nestedList: List[NestedInteger]) -> int:
        """
        Calculates the weighted sum of integers in a nested list based on their depth.

        Args:
            nestedList (List[NestedInteger]): The nested list of integers and lists.

        Returns:
            int: The weighted sum of integers.
        """
        depth = 1
        res = 0
        queue = deque(nestedList)

        while queue:
            for _ in range(len(queue)):
                cur = queue.popleft()
                if cur.isInteger():
                    res += cur.getInteger() * depth
                else:
                    queue.extend(cur.getList())
            depth += 1

        return res
