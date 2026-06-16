from collections import deque
class Solution:
    def isValid(self, s: str) -> bool:
        stack = deque()
        for i in range(len(s)):
            if s[i] == '(' or s[i] == '[' or s[i] == '{':
                stack.append(s[i])
            else:
                if not stack:
                    return False
                else:
                    top = stack[-1]
                    if s[i] == ')' and top != '(':
                        return False
                    if s[i] == ']' and top != '[':
                        return False
                    if s[i] == '}' and top != '{':
                        return False
                    stack.pop()
        return len(stack) == 0