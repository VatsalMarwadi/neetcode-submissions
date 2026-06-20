from collections import deque
class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        ans = [0] * len(temperatures)
        stack = deque()
        for i in range(len(temperatures)):
            while stack and temperatures[i] > temperatures[stack[-1]]:
                p = stack.pop()
                ans[p] = i - p
            stack.append(i)
        return ans