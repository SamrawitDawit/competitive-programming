from collections import defaultdict
class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        rows, cols, boxes = defaultdict(list), defaultdict(list), defaultdict(list)
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    if board[i][j] in rows[i]:
                        return False
                    if board[i][j] in cols[j]:
                        return False 
                    if board[i][j] in boxes[(i//3, j//3)]:
                        return False
                    rows[i].append(board[i][j])
                    cols[j].append(board[i][j])
                    boxes[(i//3,j//3)].append(board[i][j])  
        return True