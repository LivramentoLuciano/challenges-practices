######### LeetCode Problem N°48 - Rotate Image (Medium) ################
# You are given an n x n 2D matrix representing an image,rotate the image by 90 degrees (clockwise).
# You have to rotate the image in-place, which means you have to modify the input 2D matrix directly.
# DO NOT allocate another 2D matrix and do the rotation.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [[7,4,1],[8,5,2],[9,6,3]]
#
# Example 2:
# Input: matrix = [[5,1,9,11],[2,4,8,10],[13,3,6,7],[15,14,12,16]]
# Output: [[15,13,2,5],[14,3,4,1],[12,6,8,9],[16,7,10,11]]
#
# Constraints:
# n == matrix.length == matrix[i].length
# 1 <= n <= 20
# -1000 <= matrix[i][j] <= 1000

class Solution:
    def rotate(self, matrix: list[list[int]]) -> None:
        ''' 
        Rotación de una matriz, in-place. 
        Rotar 90° equivale a tomar la matriz de abajo hacia arriba
        y luego convertir las columnas a filas.
        
        >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
        >>> rotate(matrix)
        None
        # matrix = [[7,4,1],[8,5,2],[9,6,3]]
        '''
        # 1. Bottom-up -> matrix[::-1]
        # 2. Conversión columnas a filas: 
        #    -> desempaquetado (*) + Agrupar elem 'i' de cada fila (zip)
        #    -> m[:] = zip(*m)   (equivale a m=list(zip(*m)))
        # matrix[:] = zip(*matrix[::-1])   

        # Solución anterior, en realidad devuelve array de tuplas (zip)
        # Se puede mapear cada uno a lista
        matrix[:] = map(list, zip(*matrix[::-1]))
        return None

class SolutionListCompr:
    def rotate(self, matrix: list[list[int]]) -> None:
        ''' 
        Rotación de una matriz, in-place. 
        Rotar 90° equivale a tomar la matriz de abajo hacia arriba
        y luego convertir las columnas a filas.
        
        >>> matrix = [[1,2,3],[4,5,6],[7,8,9]]
        >>> rotate(matrix)
        None
        # matrix = [[7,4,1],[8,5,2],[9,6,3]]
        '''
        matrix[:] = [
            [row[i] for row in matrix[::-1]]
            for i in range(len(matrix))
        ]

        return matrix

test1 = {
    'matrix_in': [[1,2,3], [4,5,6], [7,8,9]],
    'matrix': [[1,2,3], [4,5,6], [7,8,9]], 
    'output_exp': [[7,4,1],[8,5,2],[9,6,3]]
}

test2 = {
    'matrix': [[1,2],[3,4]], 
    'output-exp': [[3,1],[4,2]]
}

tests = [test1]
for test in tests:
    res = SolutionListCompr().rotate(test['matrix'])
    print('Matriz entrada: {}\nResultado esperado: {}\nResultado (in-place): {}'\
        .format(test['matrix_in'], test['output_exp'], test['matrix']))
    print('-'*75)


