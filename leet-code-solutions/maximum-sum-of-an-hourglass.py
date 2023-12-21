class Solution:
    def maxSum(self, grid: List[List[int]]) -> int:
        maximum = 0
        for row in range(len(grid)-2):
            for colum in range(len(grid[row])-2):
                maximum = max(maximum, grid[row][colum] + grid[row][colum+1]+ grid[row][colum+2]+grid[row+1][colum+1]+ grid[row+2][colum]+grid[row+2][colum+1]+ grid[row+2][colum+2])
        return maximum