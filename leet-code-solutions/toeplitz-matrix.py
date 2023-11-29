class Solution:
    def isToeplitzMatrix(self, matrix: List[List[int]]) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        if m < 2 or n < 2:
            return True
        
        for row in range(m-1):
            for column in range(n-1):
                if matrix[row][column] != matrix[row+1][column+1]:
                    return False
        return True