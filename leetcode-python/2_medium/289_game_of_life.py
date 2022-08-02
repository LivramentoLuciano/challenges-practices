######### LeetCode Problem N°289 - Game Of Life (Medium) ################
# According to Wikipedia's article: "The Game of Life, also known simply as Life,
# is a cellular automaton devised by the British mathematician John Horton Conway in 1970."
# The board is made up of an m x n grid of cells, where each cell has an initial state: 
# live (represented by a 1) or dead (represented by a 0). Each cell interacts with its 
# eight neighbors (horizontal, vertical, diagonal) using the following four rules 
# (taken from the above Wikipedia article):
#   - Any live cell with fewer than two live neighbors dies as if caused by under-population.
#   - Any live cell with two or three live neighbors lives on to the next generation.
#   - Any live cell with more than three live neighbors dies, as if by over-population.
#   - Any dead cell with exactly three live neighbors becomes a live cell, as if by reproduction.
#   - The next state is created by applying the above rules simultaneously to every cell in 
#     the current state, where births and deaths occur simultaneously. Given the current state of 
#     the m x n grid board, return the next state.
#
# Example 1:
# Input: board = [[0,1,0],[0,0,1],[1,1,1],[0,0,0]]
# Output: [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]
#
# Example 2:
# Input: board = [[1,1],[1,0]]
# Output: [[1,1],[1,1]]
#
# Constraints:
# m == board.length
# n == board[i].length
# 1 <= m, n <= 25
# board[i][j] is 0 or 1.

# Solución sin utilizar espacio extra. Space: O(1)
class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        '''Do not return anything, modify board in-place instead.'''
        # Algoritmo:
        # Mismo concepto que en la solución anterior, pero ahora modificaré
        # sobre la marcha las celdas de la tabla original, pero deberé hacerlo
        # de tal manera que el estado marcado no afecte al estado futuro de los vecinos
        def analyzeCell(i, j):
            '''
            Analiza una celda del Game Of Life, devolviendo el valor que deberá tomar
            en función de sus vecinos del tablero.
            '''
            live_neighbours = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if (0 <= ii < m) and (0 <= jj < n) and (ii,jj) != (i,j):
                        if board[ii][jj] in [1, FUTURE_ZERO] :
                            live_neighbours += 1
            
            if board[i][j] == 0: 
                return live_neighbours == 3

            return 2 <= live_neighbours <= 3        

        # Marcas para convertir 1's a 0's y viceversa. El resto queda igual
        FUTURE_ONE, FUTURE_ZERO = '1', '0'

        m, n = len(board), len(board[0])
        for i in range(m):
            for j in range(n):
                c = board[i][j]
                # Si es un 0 y tengo que revivirlo, marco con '1'
                if c == 0 and analyzeCell(i, j): 
                    board[i][j] = FUTURE_ONE

                # Si es un 1 y tengo que matarlo, marco con '0'
                if c == 1 and not analyzeCell(i, j): 
                    board[i][j] = FUTURE_ZERO

        # Finalmente, hago efectiva las conversiones a 1 y 0
        board[:] = [
            [ int(c) if c in [FUTURE_ZERO, FUTURE_ONE] else c for c in row ] 
            for row in board
        ]


# NOTE: Solución Inicial. Space: O(N)
class SolutionIni:
    def gameOfLife(self, board: list[list[int]]) -> None:
        '''Do not return anything, modify board in-place instead.'''
        def analyzeCell(i, j):
            '''
            Analiza una celda del Game Of Life, devolviendo el valor que deberá tomar
            en función de sus vecinos del tablero.
            '''
            live_neighbours = 0
            for ii in range(i-1, i+2):
                for jj in range(j-1, j+2):
                    if (0 <= ii < m) and (0 <= jj < n) and (ii,jj) != (i,j):
                        if board[ii][jj] == 1:
                            live_neighbours += 1
            
            if board[i][j] == 0: 
                return live_neighbours == 3

            return 2 <= live_neighbours <= 3

        # La primera solucion sería utilizando una tabla extra para ir guardando los valores futuros
        m, n = len(board), len(board[0])
        aux = [[0 for _ in range(n)] for _ in range(m)]

        for i in range(m):
            for j in range(n):
                aux[i][j] = 1 if analyzeCell(i, j) else 0
        
        board[:] = aux[:]
        return 


# Pruebas
test1 = {'board_orig': [[0,1,0],[0,0,1],[1,1,1],[0,0,0]], 'board': [[0,1,0],[0,0,1],[1,1,1],[0,0,0]], 'output_exp': [[0,0,0],[1,0,1],[0,1,1],[0,1,0]]}
test2 = {'board_orig': [[1,1],[1,0]], 'board': [[1,1],[1,0]], 'output_exp': [[1,1],[1,1]]}
tests = [test1, test2]
tests = [test1]
for test in tests:
    Solution().gameOfLife(test['board'])
    print('board: {} - Resultado esperado: {} - Resultado: {}'.format(test['board_orig'], test['output_exp'], test['board']))
        