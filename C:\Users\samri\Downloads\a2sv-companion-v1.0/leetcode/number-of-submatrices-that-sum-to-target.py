class Solution:
    def numSubmatrixSumTarget(self, matrix: List[List[int]], target: int) -> int:
        rows = len(matrix)
        cols = len(matrix[0])
        prefix_matrix = [[0]*cols for row in range(rows)]
        ans = 0
        for row in range(rows):
            for col in range(cols):
                top = prefix_matrix[row-1][col] if row > 0 else 0
                left = prefix_matrix[row][col-1] if col > 0 else 0
                top_left = prefix_matrix[row-1][col-1] if row*col > 0 else 0
                prefix_matrix[row][col] = (matrix[row][col]+ top + left) - top_left
        for row1 in range(rows):
            for row2 in range(row1, rows):
                prefix_dic = {}
                prefix_dic[0] = 1
                for col in range(cols):
                    top = prefix_matrix[row1-1][col] if row1 > 0 else 0
                    curr_sum = prefix_matrix[row2][col]- top
                    ans += prefix_dic.get((curr_sum-target), 0)
                    prefix_dic[curr_sum] = prefix_dic.get(curr_sum, 0) + 1
        return ans

