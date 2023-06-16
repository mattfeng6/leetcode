# https://leetcode.com/problems/valid-parentheses/

class Solution:
    def isValid(self, s: str) -> bool:

        if not s: return False

        stack = []

        for char in s:
            if not stack:
                stack.append(char)
            else:
                if stack[-1] == '(' and char == ')':
                    stack.pop()
                elif stack[-1] == '[' and char == ']':
                    stack.pop()
                elif stack[-1] == '{' and char == '}':
                    stack.pop()
                else: 
                    stack.append(char)

        return not stack

# BlackRock