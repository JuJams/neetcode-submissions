class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        # Checking rows for duplicates
        for row in range(9):
            for i in range(9):
                # print (board[row][i])
                if board[row][i] == '.':
                    continue
                for j in range(i+1, 9):
                    if board[row][i] == board[row][j]:
                        return False
        # Checking columns for duplicates
        for col in range(9):
            for i in range(9):
                if board[i][col] == '.':
                    continue
                for j in range(i+1,9):
                    if board[i][col] == board[j][col]:
                        return False 
        # Checking for the 3*3 boxes
        for box_row in range(0,9,3):
            for box_col in range(0,9,3):
                for k1 in range(9):
                    r1 = box_row + k1//3
                    c1 = box_col + k1 % 3
                    if board[r1][c1] == '.':
                        continue
                    for k2 in range(k1+1,9):
                        r2 = box_row + k2//3
                        c2 = box_col + k2 % 3
                        if board[r1][c1] == board[r2][c2]:
                            return False
        return True
         
            