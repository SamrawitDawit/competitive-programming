class Solution:
    def countUnguarded(self, m: int, n: int, guards: List[List[int]], walls: List[List[int]]) -> int:
        matrix = [[0]*n for row in range(m)]
        for guard in guards:
            matrix[guard[0]][guard[1]] = 'G'
        for wall in walls:
            matrix[wall[0]][wall[1]] = 'W'
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 'G':
                    indx = i-1
                    while indx >= 0 and (matrix[indx][j] == 0 or matrix[indx][j] == 'GU'):
                        matrix[indx][j] = 'GU'
                        indx -= 1
                    indx = i+1
                    while indx < m and (matrix[indx][j] == 0 or matrix[indx][j] == 'GU'):
                        matrix[indx][j] = 'GU'
                        indx += 1
                    indx = j-1
                    while indx >= 0 and (matrix[i][indx] == 0 or matrix[i][indx] == 'GU'):
                        matrix[i][indx] = 'GU'
                        indx -= 1
                    indx = j+1
                    while indx < n and (matrix[i][indx] == 0 or matrix[i][indx] == 'GU'):
                        matrix[i][indx] = 'GU'
                        indx += 1
        print(matrix)
        guarded = 0
        for row in matrix:
            guarded += row.count('GU')
        return m*n -(len(guards) + len(walls)+guarded)
        
                    