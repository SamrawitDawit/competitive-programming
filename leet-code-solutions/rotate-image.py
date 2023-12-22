class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """
        Do not return anything, modify matrix in-place instead.
        """
        for row in range(len(matrix)):
            for colum in range(row, len(matrix[0])):
                matrix[row][colum], matrix[colum][row] = matrix[colum][row], matrix[row][colum]
        for row in matrix:
            row.reverse()