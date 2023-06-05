# https://leetcode.com/problems/letter-combinations-of-a-phone-number/

from typing import List

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        

        conversion = {
            2: ["a", "b", "c"],
            3: ["d", "e", "f"],
            4: ["g", "h", "i"],
            5: ["j", "k", "l"],
            6: ["m", "n", "o"],
            7: ["p", "q", "r", "s"],
            8: ["t", "u", "v"],
            9: ["w", "x", "y", "z"]
        }

        result = []

        for digit in digits:
            curr = conversion[int(digit)]
            
            if result == []: result = curr
            else:
                next = []
                for prevElement in result:
                    for currElement in curr:
                        next.append(prevElement + currElement)
                result = next
      
        return result