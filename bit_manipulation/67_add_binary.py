# https://leetcode.com/problems/add-binary/
# https://leetcode.com/problems/add-binary/solutions/279879/python-easy-to-understand/

class Solution:
    def addBinary(self, a: str, b: str) -> str:

        carry = 0
        res = ''

        a, b = list(a), list(b)

        while a or b or carry:
            if a:
                carry += int(a.pop())
            if b:
                carry += int(b.pop())

            res += str(carry % 2)
            carry //= 2

        return res[::-1]