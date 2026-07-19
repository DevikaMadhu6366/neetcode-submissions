class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        match = {')': '(', ']': '[', '}': '{'}

        for c in s:
            if c == '(' or c == '[' or c == '{':
                stack.append(c)
            elif not stack or stack.pop() != match[c]:
                return False

        return not stack