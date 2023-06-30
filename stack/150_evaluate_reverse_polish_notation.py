# https://leetcode.com/problems/evaluate-reverse-polish-notation/

from typing import List

class Solution:
    def evalRPN(self, tokens: List[str]) -> int:

        stack = []

        operations = ['+', '-', '*', '/']
        for token in tokens:
            if token in operations:
                x, y = int(stack.pop()), int(stack.pop())
                stack.append(x+y if token=='+' else y-x if token=='-' else x*y if token=='*' else int(y/x))
            else:
                stack.append(token)

        return int(stack[-1])