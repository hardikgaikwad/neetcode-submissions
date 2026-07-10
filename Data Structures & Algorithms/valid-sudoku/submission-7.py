class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols = defaultdict(set), defaultdict(set)
        squares = defaultdict(set)
        for r in range(9):
            for c in range(9):
                if board[r][c] == '.': continue
                squareKey = (r//3, c//3)
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or 
                    board[r][c] in squares[squareKey]):
                    return False
                rows[r].add(board[r][c])
                cols[c].add(board[r][c])
                squares[squareKey].add(board[r][c])
        return True