class Solution:
    def solveNQueens(self, n: int) -> List[List[str]]:
        col_set, sum_diagonal, diff_diagonal = set(), set(), set()
        ans = []
        puzzle = [['.']*n for row in range(n)]
        def backtrack(r):
            if r == n:
                ans.append([''.join(row) for row in puzzle])
                return
            for c in range(n):
                if c in col_set or r+c in sum_diagonal or r-c in diff_diagonal:
                    continue
                col_set.add(c)
                sum_diagonal.add(r+c)
                diff_diagonal.add(r-c)
                puzzle[r][c] = 'Q'
                backtrack(r+1)
                col_set.remove(c)
                sum_diagonal.remove(r+c)
                diff_diagonal.remove(r-c)
                puzzle[r][c] = '.'
        backtrack(0)
        return ans


        
                


