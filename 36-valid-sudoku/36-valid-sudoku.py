class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows = set()
        cols = set()
        boxes = set()
        for i in range(9):
            for j in range(9):
                n = board[i][j]
                if n=='.':continue
                if (i,n) in rows or (j,n) in cols or (i//3,j//3,n) in boxes:
                    return False
                rows.add((i,n))
                cols.add((j,n))
                boxes.add((i//3,j//3,n))
        return True