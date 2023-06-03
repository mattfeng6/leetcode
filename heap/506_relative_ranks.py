# https://leetcode.com/problems/relative-ranks/

from typing import List 
import heapq

class Solution:
    def findRelativeRanks(self, score: List[int]) -> List[str]:

        # Heap (Priority Queue)

        rankings = []
        for index, value in enumerate(score):
            heapq.heappush(rankings, (-value, index))

        res = [""] * len(score)
        rank = 1
        while len(rankings) != 0:
            _, i = heapq.heappop(rankings)
            if rank == 1:
                res[i] = "Gold Medal"
            elif rank == 2:
                res[i] = "Silver Medal"
            elif rank == 3:
                res[i] = "Bronze Medal"
            else:
                res[i] = f'{rank}'
            rank += 1

        return res