from typing import List
from collections import Counter
from collections import deque
import heapq

class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        """
        Calculates the minimum time required to complete all tasks with a cooldown of `n`
        units of time between two identical tasks.

        Args:
            tasks (List[str]): A list of tasks represented by uppercase letters ('A' to 'Z').
            n (int): The cooldown period between two identical tasks.

        Returns:
            int: The minimum time units required to complete all tasks.
        """

        freq = [0] * 26
        for task in tasks:
            freq[ord(task) - ord('A')] += 1

        max_freq = max(freq)
        freq_count = freq.count(max_freq)

        total_gaps = n * (max_freq - 1)
        fillers_available = len(tasks) - max_freq

        idles = total_gaps - fillers_available + (freq_count - 1)

        return len(tasks) + max(0,idles)

    def leastInterval_heap(self, tasks: List[str], n: int) -> int:
        """
        Calculates the minimum time required to complete all tasks with a cooldown of `n`
        units of time between two identical tasks using a max-heap approach.

        Args:
            tasks (List[str]): A list of tasks represented by uppercase letters ('A' to 'Z').
            n (int): The cooldown period between two identical tasks.

        Returns:
            int: The minimum time units required to complete all tasks.
        """

        count = Counter(tasks)
        maxHeap = [-cnt for cnt in count.values()]
        heapq.heapify(maxHeap)

        time = 0
        tasks_on_hold = deque()

        while maxHeap or tasks_on_hold:
            time += 1
            if maxHeap:
                cnt = 1 + heapq.heappop(maxHeap)
                if cnt != 0:
                    tasks_on_hold.append([cnt, time + n])
            if tasks_on_hold and tasks_on_hold[0][1] == time:
                heapq.heappush(maxHeap, tasks_on_hold.popleft()[0])

        return time