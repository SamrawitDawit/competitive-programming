class Solution:
    def maxIncreaseKeepingSkyline(self, grid: List[List[int]]) -> int:
        row_max = {}
        col_max = {}
        for row in range(len(grid)):
            maxx = grid[row][0]
            for col in range(1, len(grid[0])):
                maxx = max(maxx, grid[row][col])
            row_max[row] = maxx
        for col in range(len(grid[0])):
            maxx = grid[0][col]
            for row in range(len(grid)):
                maxx = max(maxx, grid[row][col])
            col_max[col] = max(maxx, grid[row][col])
        summ = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                summ += (min(row_max[row], col_max[col]) - grid[row][col])
        return summ


        