##################### LeetCode Problem N° 73: Set Matrix Zeroes (Medium) ########################
# Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.
# You must do it in place.
#
# Example 1:
# Input: matrix = [[1,1,1],[1,0,1],[1,1,1]]
# Output: [[1,0,1],[0,0,0],[1,0,1]]
#
# Example 2:
# Input: matrix = [[0,1,2,0],[3,4,5,2],[1,3,1,5]]
# Output: [[0,0,0,0],[0,4,5,0],[0,3,1,0]]
#
# Constraints:
# m == matrix.length
# n == matrix[0].length
# 1 <= m, n <= 200
# -231 <= matrix[i][j] <= 231 - 1
#
# Follow up:
# A straightforward solution using O(mn) space is probably a bad idea.
# A simple improvement uses O(m + n) space, but still not the best solution.
# Could you devise a constant space solution?

class Solution:
    ''' Solución Optimizada Space: O(1) (Óptima) '''
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ''' Do not return anything, modify matrix in-place instead. '''
        # En este caso, no utilizo Sets para guardar registro de las
        # filas y columnas que tienen al menos un 0
        # Directamente, recorro la matriz y realizo marcas (#) sobre los 
        # elementos distintos de 0 (de la fila y columna que tenga un 0),
        # tal que luego de recorrerla toda simplemente vuelvo a recorrerla
        # y donde vea una marca pongo un 0
        m, n = len(matrix), len(matrix[0])

        # Primer recorrido, marco toda la fila y columna al encontrar un 0
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    self.tag_row_col(matrix, i, j)
                    
        # Luego, Seteo a 0 todos los elementos previamente marcados       
        for i in range(m):
            for j in range(n):
                if matrix[i][j] == '#':
                    matrix[i][j] = 0
    
    def tag_row_col(self, matrix, row, col):
        '''Realizo marca '#' sobre la fila y columna indicada, para luego poder rellenar con 0's'''
        # Marco la fila
        for j in range(len(matrix[0])):
            if matrix[row][j] != 0:
                matrix[row][j] = '#'
        
        # Marco la columna
        for i in range(len(matrix)):
            if matrix[i][col] != 0:
                matrix[i][col] = '#'
        
class SolutionA:
    '''
    Solución utilizando Sets para guardar las filas y columnas que tienen 0's
    Space: O(m+n) (Pide optimizar más aún)
    '''
    def setZeroes(self, matrix: list[list[int]]) -> None:
        ''' Do not return anything, modify matrix in-place instead. '''
        # Se me ocurre el siguiente algoritmo
        # Busco todos los 0's en la matrix y guardo, 
        # todas las filas (i) que tengan al menos 1 zero
        # todas las column (j) que tengan al menos 1 zero
        # Luego, seteo a 0 todas las anteriores
        m, n = len(matrix), len(matrix[0])
        rows_with_zero, cols_with_zero = set(), set()

        for i in range(m):
            for j in range(n):
                if matrix[i][j] == 0:
                    rows_with_zero.add(i)
                    cols_with_zero.add(j)
        
        # Coloco 0's en las filas y columnas registradas
        for row in rows_with_zero:
            matrix[row] = [0]*n

        for col in cols_with_zero:
            for i in range(m):
                matrix[i][col] = 0
            

# Pruebas
test1 = {'matrix_orig': [[1,1,1],[1,0,1],[1,1,1]], 'matrix': [[1,1,1],[1,0,1],[1,1,1]], 'output_exp': [[1,0,1],[0,0,0],[1,0,1]]}
test2 = {'matrix_orig': [[0,1,2,0],[3,4,5,2],[1,3,1,5]], 'matrix': [[0,1,2,0],[3,4,5,2],[1,3,1,5]], 'output_exp': [[0,0,0,0],[0,4,5,0],[0,3,1,0]]}
tests = [test1, test2]
tests = [test2]
for test in tests:
    Solution().setZeroes(test['matrix'])
    print('matrix: {} - Resultado esperado: {} - Resultado: {}'.format(test['matrix_orig'], test['output_exp'], test['matrix']))
