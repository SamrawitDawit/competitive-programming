class Solution:
    def solveSudoku(self, board: List[List[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        rows, cols, boxes = defaultdict(set), defaultdict(set), defaultdict(set)
        not_filled = deque([])
        for i in range(9):
            for j in range(9):
                if board[i][j] != '.':
                    rows[i].add(board[i][j])
                    cols[j].add(board[i][j])
                    boxes[(i//3,j//3)].add(board[i][j])
                else:
                    not_filled.append((i, j)) 
        def backtrack():
            if not not_filled:
                return True
            r,c = not_filled[0]
            for num in range(1, 10):
                num = str(num)
                if (num not in rows[r] and
                num not in cols[c] and 
                num not in boxes[(r//3, c//3)]):
                    board[r][c] = num
                    rows[r].add(num)
                    cols[c].add(num)
                    boxes[(r//3, c//3)].add(num)
                    not_filled.popleft()               
                    if backtrack():
                       return True
                    board[r][c] = '.'
                    rows[r].discard(num)
                    cols[c].discard(num)
                    boxes[r//3, c//3].discard(num)
                    not_filled.appendleft((r, c))
            return False
        backtrack()
      