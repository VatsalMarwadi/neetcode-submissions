class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        row = set()
        col = set()
        boxes = set()
        for r in range(9):
            for c in range(9):
                num = board[r][c]
                if num == '.':
                    continue
                if (r, num) in row:
                    return False
                if (c, num) in col:
                    return False
                if ((r // 3, c // 3), num) in boxes:
                    return False
                row.add((r, num))
                col.add((c, num))
                boxes.add(((r // 3, c // 3), num))
        return True