class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        diagonals = collections.defaultdict(list)
        for row in range(len(mat)):
            for colum in range(len(mat[0])):
                diagonals[abs(row+colum)].append(mat[row][colum])
        output = []
        reverse = True
        for diagonal in diagonals.values():
            if reverse:
                output += reversed(diagonal)
                reverse = False
            else:
                output += diagonal
                reverse = True
        return output
