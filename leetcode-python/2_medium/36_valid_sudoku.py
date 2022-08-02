######### LeetCode Problem N°36 - Valid Sudoku (Medium) ################
# Determine if a 9 x 9 Sudoku board is valid. Only the filled cells 
# need to be validated according to the following rules:
#   - Each row must contain the digits 1-9 without repetition.
#   - Each column must contain the digits 1-9 without repetition.
#   - Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.
#
# Note:
#   - A Sudoku board (partially filled) could be valid but is not necessarily solvable.
#   - Only the filled cells need to be validated according to the mentioned rules.
# 
# Example 1:
# Input: board = 
# [["5","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: true
#
# Example 2:
# Input: board = 
# [["8","3",".",".","7",".",".",".","."]
# ,["6",".",".","1","9","5",".",".","."]
# ,[".","9","8",".",".",".",".","6","."]
# ,["8",".",".",".","6",".",".",".","3"]
# ,["4",".",".","8",".","3",".",".","1"]
# ,["7",".",".",".","2",".",".",".","6"]
# ,[".","6",".",".",".",".","2","8","."]
# ,[".",".",".","4","1","9",".",".","5"]
# ,[".",".",".",".","8",".",".","7","9"]]
# Output: false
# Explanation: Same as Example 1, except with the 5 in the top left corner being 
# modified to 8. Since there are two 8's in the top left 3x3 sub-box, it is invalid.
#
# Constraints:
# board.length == 9
# board[i].length == 9
# board[i][j] is a digit 1-9 or '.'.

class SolutionA:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        '''
        Dado un tablero de Sudoku, verifica que el mismo sea válido.
        Para ello debe cumplirse:
            - Ningún casillero de una misma fila podrá tener el mismo valor
            - Ningún casillero de una misma columna podrá tener el mismo valor
            - Ningún casillero de una misma cuadrilla interna podrá tener el mismo valor
        '''
        is_valid_row = self.is_valid_rows(board)
        is_valid_column = self.is_valid_columns(board)
        is_valid_box = self.is_valid_boxes(board)

        return is_valid_row and is_valid_column and is_valid_box

    def is_valid_rows(self, board: list[list[str]]) -> bool:
        '''Dado un Tablero de sudoku, verifica que todas sus filas sean válidas'''
        # chequeo filas
        for row in board:
            row_values = {}
            for val in row:
                if val != '.' and val in row_values:
                    return False
                else:
                    row_values[val] = row_values.get(val, 0) + 1
        return True
    
    def is_valid_columns(self, board: list[list[str]]) -> bool:
        '''Dado un Tablero de sudoku, verifica que todas sus columnas sean válidas'''
        n = len(board)        
        for col in range(n):
            col_values = {}
            for row in range(n):
                val = board[row][col]
                if val != '.' and val in col_values:
                    print(val, 'repetido en columna', col, 'fila', row)
                    return False
                else:
                    col_values[val] = col_values.get(val, 0) + 1        
        return True

    def is_valid_boxes(self, board: list[list[str]]) -> bool:
        '''Dado un Tablero de sudoku, verifica que todas sus cuadrículas interiores sean válidas'''
        for ii in range(3):
            for jj in range(3):
                # leo la box (ii, jj)
                box = []
                for row in board[3*ii:3*ii+3]:
                    box.extend(row[3*jj:3*jj+3])   
                # filtro '.' y verifico no haya repetidos                 
                box = [val for val in box if val != '.']
                for i in range(len(box)):
                    if box[i] != '.' and box[i] in box[i+1:]:
                        return False
                       
        return True


from collections import Counter
class Solution:
    '''
    Verificación de Sudoku. 
    Solución post-construcción de la fila/col/cuadrilla, usando Counter o Set
    '''
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        '''
        Dado un tablero de Sudoku, verifica que el mismo sea válido.
        Para ello debe cumplirse:
            - Ningún casillero de una misma fila podrá tener el mismo valor
            - Ningún casillero de una misma columna podrá tener el mismo valor
            - Ningún casillero de una misma cuadrilla interna podrá tener el mismo valor
        '''
        is_valid_row = self.is_valid_rows(board)
        is_valid_column = self.is_valid_columns(board)
        is_valid_box = self.is_valid_boxes(board)

        return is_valid_row and is_valid_column and is_valid_box

    def is_valid_rows(self, board: list[list[str]]) -> bool:
        '''Dado un Tablero de sudoku, verifica que todas sus filas sean válidas'''
        # Chequeo Row (contando apariciones de cada letra)
        for row in board:
            if not self.is_valid_line_counter(row):
                return False
        return True
    
    def is_valid_columns(self, board: list[list[str]]) -> bool:
        '''Dado un Tablero de sudoku, verifica que todas sus columnas sean válidas''' 
        # chequeo columnas (contando apariciones de cada letra)
        n = len(board)        
        for col in range(n):
            col = [ board[i][col] for i in range(n) ]
            if not self.is_valid_line_counter(col):
                return False
        return True

    def is_valid_boxes(self, board: list[list[str]]) -> bool:
        '''Dado un Tablero de sudoku, verifica que todas sus cuadrículas interiores sean válidas'''
        # chequeo boxes
        for ii in range(3):
            for jj in range(3):
                box = []
                for row in board[3*ii:3*ii+3]:
                    box.extend(row[3*jj:3*jj+3])
                if not self.is_valid_line_counter(box):
                    return False        
        return True

    def is_valid_line_counter(self, line:list[str]) -> bool:
        '''
        Función base de verificación de validez de una línea (fila, col, box).
        Chequea que todos sus elementos sean distintos, mediante Counter.
        '''
        # primero elimino los '.', luego verifico que no haya repetidos
        line = [val for val in line if val != '.']
        counter = Counter(line)
        return all([count == 1 for count in counter.values()])  

    def is_valid_line_set(self, line:list[str]) -> bool:
        '''
        Función base de verificación de validez de una línea (fila, col, box).
        Chequea que todos sus elementos sean distintos, mediante Set.
        '''
        # primero elimino los '.', luego verifico que no haya repetidos 
        # (comparando el tamaño del Set contra el de la lista original)
        line = [val for val in line if val != '.']
        return len(set(line)) == len(line)


test1 = {
    'board': [["5","3",".",".","7",".",".",".","."],\
              ["6",".",".","1","9","5",".",".","."],\
              [".","9","8",".",".",".",".","6","."],\
              ["8",".",".",".","6",".",".",".","3"],\
              ["4",".",".","8",".","3",".",".","1"],\
              ["7",".",".",".","2",".",".",".","6"],\
              [".","6",".",".",".",".","2","8","."],\
              [".",".",".","4","1","9",".",".","5"],\
              [".",".",".",".","8",".",".","7","9"]],
    'out_exp': True
}
tests = [test1]
for test in tests:
    res =SolutionA().isValidSudoku(test['board'])
    print('board:')
    for row in test['board']: print(row)
    print('Resultado esperado: {} - Resultado: {}'.format(test['out_exp'], res))
