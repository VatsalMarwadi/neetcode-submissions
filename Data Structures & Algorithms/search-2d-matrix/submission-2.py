class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        x = len(matrix)
        y = len(matrix[0])
        low = 0
        high = (x * y) - 1
        while low <= high:
            mid = (low + high) // 2
            row = mid // y
            col = mid % y
            val = matrix[row][col]
            if val == target:
                return True
            elif val < target:
                low = mid + 1
            else:
                high = mid - 1
        return False

        