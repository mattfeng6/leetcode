# https://leetcode.com/problems/find-common-characters/
# https://github.com/youngyangyang04/leetcode-master/blob/master/problems/1002.%E6%9F%A5%E6%89%BE%E5%B8%B8%E7%94%A8%E5%AD%97%E7%AC%A6.md

from typing import List
import collections

class Solution:
    def commonChars(self, words: List[str]) -> List[str]:

        temp = collections.Counter(words[0])
        l = []
        for i in range(1, len(words)):
            temp = temp & collections.Counter(words[i])

        for j in temp:
            v = temp[j]
            while v:
                l.append(j)
                v -= 1
        return l  