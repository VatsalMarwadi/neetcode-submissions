from collections import deque
class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stack = deque()
        for i in tokens:
            if i in  {'+', '-', '*', '/'}:
                b = stack.pop()
                a = stack.pop()
                if i == '+':
                    stack.append(a + b)
                elif i == '-':
                    stack.append(a - b)
                elif i == '*':
                    stack.append(a * b)
                else:
                    stack.append(int(float(a) / b))
            else:
                stack.append(int(i))
        return stack.pop()