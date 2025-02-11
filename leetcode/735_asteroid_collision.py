from typing import List

class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        """Simulates asteroid collisions and returns the surviving asteroids.

        Args:
            asteroids (List[int]): A list of integers representing asteroids,
                                   where positive values move right and negative values move left.

        Returns:
            List[int]: The state of asteroids after all collisions.
        """

        stack = []

        for asteroid in asteroids:
            if asteroid > 0:
                stack.append(asteroid)
            else:
                while stack and -asteroid > stack[-1] > 0:
                    stack.pop()
                if not stack or stack[-1] < 0:
                    stack.append(asteroid)
                elif stack[-1] == -asteroid:
                    stack.pop()

        return stack
