class Solution:
    def transpose(self, matrix: List[List[int]]) -> List[List[int]]:
        transpose_matrix = [[0]*len(matrix) for colum in range(len(matrix[0]))]
        for row in range(len(transpose_matrix)):
            for colum in range(len(transpose_matrix[0])):
                transpose_matrix[row][colum] = matrix[colum][row]
        return transpose_matrix