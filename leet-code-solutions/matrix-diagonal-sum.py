class Solution:
    def diagonalSum(self, mat: List[List[int]]) -> int:
        i, j = 0, 0
        summ = 0
        n = len(mat)
        for cell in range(n):
            summ += mat[i][j]
            i += 1
            j += 1
        i, j = 0, n-1
        for cell in range(n):
            summ += mat[i][j]
            i += 1
            j -= 1
        if n % 2 != 0:
            n = n//2
            summ -= mat[n][n]
        return summ

