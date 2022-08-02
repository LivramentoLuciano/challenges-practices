########## LeetCode Problem N°200 - Number of Islands (Medium) ################
# Given an m x n 2D binary grid grid which represents a map of '1's (land) 
# and '0's (water), return the number of islands.
# An island is surrounded by water and is formed by connecting adjacent lands 
# horizontally or vertically. You may assume all four edges of the grid are all surrounded by water.
#
# Example 1:
# Input: grid = [
#   ["1","1","1","1","0"],
#   ["1","1","0","1","0"],
#   ["1","1","0","0","0"],
#   ["0","0","0","0","0"]
# ]
# Output: 1
#
# Example 2:
# Input: grid = [
#   ["1","1","0","0","0"],
#   ["1","1","0","0","0"],
#   ["0","0","1","0","0"],
#   ["0","0","0","1","1"]
# ]
# Output: 3
#
# Constraints:
# m == grid.length
# n == grid[i].length
# 1 <= m, n <= 300
# grid[i][j] is '0' or '1'.

from collections import deque
class Solution:
    def numIslands(self, grid: list[list[str]]) -> int:
        # Sobre cada (i,j) recorro todos los 1's conectados a este
        # mediante una cola que busca los 1's a su alrededor
        # al finalizar con un (i,j) encontré una isla
        # La marca '#' es para evitar revisitas (loop inf)
        m, n = len(grid), len(grid[0])
        q = deque()
        count = 0

        for i in range(m):
            for j in range(n):
                if grid[i][j] == '1':
                    # Recorro todos los 1's conectados a este (i,j)
                    # El '#' es para evitar revisita (como set seen)
                    grid[i][j] = '#'
                    q.append((i,j))
                    while q:
                        r, c = q.popleft()
                        for rr, cc in [(r-1, c), (r, c+1), (r+1, c), (r, c-1)]:
                            if (0 <= rr < m) and (0 <= cc < n) and grid[rr][cc] == '1':
                                q.append((rr, cc))
                                grid[rr][cc] = '#'
                    # termino de recorrer todos los 1's conectados a (i,j)
                    # agrego al contador de islas
                    count += 1

        return count


# Pruebas
test1 = {
    'grid_orig': [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 
    'grid': [["1","1","1","1","0"],["1","1","0","1","0"],["1","1","0","0","0"],["0","0","0","0","0"]], 
    'output_exp': 1
}
test2 = {
    'grid_orig': [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 
    'grid': [["1","1","0","0","0"],["1","1","0","0","0"],["0","0","1","0","0"],["0","0","0","1","1"]], 
    'output_exp': 3
}
tests = [test1, test2]
tests = [test2]
for test in tests:
    res = Solution().numIslands(test['grid'])
    print('grid: {} - Resultado esperado: {} - Resultado: {}'.format(test['grid_orig'], test['output_exp'], res))

 