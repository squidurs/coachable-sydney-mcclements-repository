from collections import defaultdict
import heapq


class Solution1:
    """Provides a solution to reorganize a string such that no two
    adjacent characters are the same, using a max-heap approach."""
    def reorganizeString(self, s: str) -> str:
        """Uses a max-heap to append two max count characters at a time.
        Character counts are only added to the heap if reorganization is possible
        (max character count < half the string length), ensuring the final element
        can be appended without violating the adjacency rule."""


        char_count = defaultdict(int)


        for char in s:
            char_count[char] += 1


        max_heap = []


        for char, count in char_count.items():
            if count > (len(s) + 1) // 2:
                return ""
            heapq.heappush(max_heap, [-count, char])


        result = []

        while len(max_heap) >= 2:
            top_count = heapq.heappop(max_heap)
            next_count = heapq.heappop(max_heap)

            result.append(top_count[1])
            result.append(next_count[1])


            if top_count[0] + 1 != 0:
                top_count[0] += 1
                heapq.heappush(max_heap, top_count)


            if next_count[0] + 1 != 0:
                next_count[0] += 1
                heapq.heappush(max_heap, next_count)


        if max_heap:
            count, char = heapq.heappop(max_heap)
            result.append(char)


        return ''.join(result)




class Solution2:
    """Provides a solution to reorganize a string such that no two
    adjacent characters are the same, using a direct placement method."""
    def reorganizeString(self, s: str) -> str:
        """Counts character frequencies and directly places the most frequent
        character in even indices of the result array. Remaining characters are
        then filled into any remaining even indices first, then odd indices afterward."""

        char_count = [0]*26

        for char in s:
            char_count[ord(char) - ord('a')] += 1

        max_count = 0
        max_char = 0
        for i in range(26):
            if char_count[i] > max_count:
                max_count = char_count[i]
                max_char = i

        if max_count > (len(s) + 1)//2:
            return ""

        result = [""]*len(s)

        idx= 0
        while char_count[max_char] > 0:
            result[idx] = chr(max_char + ord('a'))
            idx += 2
            char_count[max_char] -= 1

        for i in range(26):
            while char_count[i] > 0:
                if idx >= len(s):
                    idx = 1
                result[idx] = chr(i + ord('a'))
                idx += 2
                char_count[i] -= 1

        return "".join(result)
    
