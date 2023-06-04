# https://leetcode.com/problems/reverse-vowels-of-a-string/

class Solution:
    def reverseVowels(self, s: str) -> str:

        def checkVowel(s: str) -> bool:
            return s == 'a' or s == 'e' or \
                s == 'i' or s == 'o' or s == 'u'

        listStr = list(s)
        left, right = 0, len(s) - 1
        while left <= right:
            if not checkVowel(listStr[left].lower()):
                left += 1
            elif not checkVowel(listStr[right].lower()):
                right -= 1
            else:
                temp = listStr[left]
                listStr[left] = listStr[right]
                listStr[right] = temp
                left += 1; right -= 1

        return ''.join(listStr)
        