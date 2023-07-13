# https://leetcode.com/problems/remove-colored-pieces-if-both-neighbors-are-the-same-color/

class Solution:
    def winnerOfGame(self, colors: str) -> bool:

        # Special Situation
        if len(colors) < 3: return False

        countA = countB = 0
        for i in range(1, len(colors)-1):
            if colors[i] == 'A' and colors[i-1] == 'A' and colors[i+1] == 'A':
                countA += 1
            if colors[i] == 'B' and colors[i-1] == 'B' and colors[i+1] == 'B':
                countB += 1

        return countA > countB
