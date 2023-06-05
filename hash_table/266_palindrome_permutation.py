# https://www.youtube.com/watch?v=Pp5hdsNdqOU&ab_channel=NickWhite

# Given a string, determine if a permutation
# of the string could form a palindrome

class Solution:
    def canPermutePalindrome(self, s: str) -> bool:
        
        Set = set()
        for char in s:
            if char in Set:
                Set.remove(char)
            else:
                Set.add(char)
        
        return len(Set) <= 1
