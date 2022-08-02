######### LeetCode Problem N°130 - Surrounded Regions (Medium) ################
# Given an m x n matrix board containing 'X' and 'O', 
# capture all regions that are 4-directionally surrounded by 'X'.
# A region is captured by flipping all 'O's into 'X's in that surrounded region.
#
# Example 1:
# Input: board = [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]]
# Output: [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]
# Explanation: Surrounded regions should not be on the border, which means that any 'O' on the border of the board are not flipped to 'X'. Any 'O' that is not on the border and it is not connected to an 'O' on the border will be flipped to 'X'. Two cells are connected if they are adjacent cells connected horizontally or vertically.
#
# Example 2:
# Input: board = [["X"]]
# Output: [["X"]]
#
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 200
# board[i][j] is 'X' or 'O'.

from collections import deque
class Solution:
    def solve(self, board: list[list[str]]) -> None:
        '''Do not return anything, modify board in-place instead.'''
        # Debo tomar las regiones  de 'O', que deben ser rodeadas por 'X', no solo las celdas
        # Entonces, la idea basica será recorrer los bordes y donde haya una O,
        # buscar todos las 'O' que estén conectadas (para cualquier costado) y marcarlas
        # luego las O que no hayan sido marcadas las convierto a X
        self.tag_boundary_connected(board)
        self.flip_regions(board)
        return None

    def tag_boundary_connected(self, board):
        '''Marco todas las O's conectadas a los bordes (por medio de otras O)'''
        # recorro los bordes top,right,left,bottom
        # agregando a una cola todos las O que encuentre (su posicion i,j)
        # luego sobre cada una de ellas, buscare en sus alrededores
        # las O conectadas y las marco con '#'
        m, n = len(board), len(board[0])
        q = deque()

        # left y right
        for r in range(m):
            if board[r][0] == 'O':
                q.append((r, 0))
            if board[r][n-1] == 'O':
                q.append((r, n-1))

        # top y bottom
        for c in range(n):
            if board[0][c] == 'O':
                q.append((0, c))
            if board[m-1][c] == 'O':
                q.append((m-1, c))

        # consumo los elementos de la cola, cada O del borde,
        # y voy buscando O's conectadas y las agrego a la cola también
        while q:
            i, j = q.popleft()
            board[i][j] = '#'
            # busco O's conectadas en sus 4 costados
            for ii,jj in [(i-1, j), (i, j+1), (i+1, j), (i, j-1)]:
                if (0 <= ii < m) and (0 <= jj < n) and board[ii][jj] == 'O':
                    q.append((ii, jj))
                    board[ii][jj] = '#'
                    
    def flip_regions(self, board):
        '''
        Flipeo a X todas las O que encuentro 
        (no fueron marcadas con # ya que no se pueden conectar a los bordes)
        '''
        # board[:] = [['O' if elem == '#' else 'X' for elem in row] for row in board]
        board[:] = [['XO'[elem=='#'] for elem in row] for row in board]


# Pruebas
test1 = {'board_orig': [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], 'board': [["X","X","X","X"],["X","O","O","X"],["X","X","O","X"],["X","O","X","X"]], 'output_exp': [["X","X","X","X"],["X","X","X","X"],["X","X","X","X"],["X","O","X","X"]]}
test2 = {'board_orig': [["X"]], 'board': [["X"]], 'output_exp': [["X"]]}
test3 = {
    'board_orig': [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]], 
    'board': [["O","X","X","O","X"],["X","O","O","X","O"],["X","O","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]], 
    'output_exp': [["O","X","X","O","X"],["X","X","X","X","O"],["X","X","X","O","X"],["O","X","O","O","O"],["X","X","O","X","O"]]
}
tests = [test1, test2]
tests = [test3]
for test in tests:
    Solution().solve(test['board'])
    print('board:')
    for row in test['board_orig']: print(row)
    print('Resultado esperado:')
    for row in test['output_exp']: print(row)    
    print('Resultado:')
    for row in test['board']: print(row)
