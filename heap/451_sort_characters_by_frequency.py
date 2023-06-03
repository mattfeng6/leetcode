# https://leetcode.com/problems/sort-characters-by-frequency/

import heapq

class Solution:
    def frequencySort(self, s: str) -> str:

        mapping = {}

        for char in s:
            if char not in mapping:
                mapping[char] = 1
            else:
                mapping[char] += 1

        ranking = []
        for key, value in mapping.items():
            heapq.heappush(ranking, (-value, key))

        res = []
        while ranking:
            value, key = heapq.heappop(ranking)
            res += [key] * -value

        return ''.join(res)