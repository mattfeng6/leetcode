# https://leetcode.com/problems/valid-palindrome/

class Solution:
    def isPalindrome(self, s: str) -> bool:
        
        s = [i for i in s.lower() if i.isalnum()]

        return s == s[::-1]