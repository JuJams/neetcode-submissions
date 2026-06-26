class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # use a hashset for every single row
        # use a hashset for every single column
        # use a hashset to show 3*3 grids
        # time: O(n) O(9^2)
        # space: O(n)
        # row check
        # col check
        cols = collections.defaultdict(set)
        rows = collections.defaultdict(set)
        squares = collections.defaultdict(set)

        for r in range(9):
            for c in range(9):
                if board[r][c] == ".":
                    continue
                if (board[r][c] in rows[r] or 
                    board[r][c] in cols[c] or
                    board[r][c] in squares[(r//3,c//3)]):
                    return False
                cols[c].add(board[r][c])
                rows[r].add(board[r][c])
                squares[(r//3,c//3)].add(board[r][c])
        return True
                
