class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        maxArea = 0
        n = len(heights)
        for i in range(n):
            height = heights[i]
            left = i
            while left >= 0 and heights[left] >= height:
                left -= 1

            right = i
            while right < n and heights[right] >= height:
                right += 1

            width = right - left - 1
            maxArea = max(maxArea, height * width)
        return maxArea