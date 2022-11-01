############ LeetCode Problem N° 118: Pascal´s Triangle II (Easy) #################
# Given an integer rowIndex, return the rowIndexth (0-indexed) row of the Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: rowIndex = 3
# Output: [1,3,3,1]
#
# Example 2:
# Input: rowIndex = 0
# Output: [1]
#
# Example 3:
# Input: rowIndex = 1
# Output: [1,1]
#
# Constraints:
# 0 <= rowIndex <= 33

class SolutionRecursive:  
    '''Solución Optimiazada con Space: O(rowIndex) mediante Recursividad'''  
    def getRow(self, rowIndex: int) -> list[int]:    
        # caso base: rowIndex = 0 
        if rowIndex == 0:
            return [1]
        
        # sino, recursividad para hallar la fila anterior
        prev_row = self.getRow(rowIndex - 1)

        # A partir de la anterior, construyo la fila de Pascal actual
        # Tener en cuenta que el primer y ultimo elemento son un '1'
        # Para cada fila, el proceso se realiza 1 vez menos que el tamaño de la anterior fila
        current_row = [1]
        for i in range(len(prev_row)-1):
            current_row.append(prev_row[i] + prev_row[i+1])
        current_row.append(1)

        return current_row

class Solution2:  
    '''Solución sin necesidad de cuadrado con relleno'''  
    def getRow(self, rowIndex: int) -> list[int]:        
        '''
        Devuelve la 'rowIndex'ésima fila del Triangulo de Pascal

        >>> getRow(3)
        [1,3,3,1]
        ''' 
        # En este caso, construyo el trinagulo directamente, rellenando con 1's
        # y construyendo solo los elementos necesarios por fila (no relleno de mas)
        triangle_size = rowIndex + 1
        triangle = [ [1]*(i+1) for i in range(triangle_size)]
        
        # recorro cada fila, ahora haciendo la sumatoria para generar el Pascal
        for row in range(triangle_size):
            for col in range(1, row):
                triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]
        
        return triangle[rowIndex]


class Solution:  
    '''Solución básica inicial, construyendo un cuadrado rellenado con 0´s '''  
    def getRow(self, rowIndex: int) -> list[int]:        
        '''
        Devuelve la 'rowIndex'ésima fila del Triangulo de Pascal

        >>> getRow(3)
        [1,3,3,1]
        '''        
        # Construccion del Triangulo de Pascal hasta el enésimo nivel (rowIndex)
        # Relleno con 1's la primera columna, el resto con 0's
        pascal_size = rowIndex + 1
        pascal_square = [ 
            [0 if i != 0 else 1 for i in range(pascal_size) ]
            for i in range(pascal_size)
        ]

        # Ahora lo recorro construyendo los elementos interiores
        for row in range(1, pascal_size):
            for col in range(1, pascal_size):
                pascal_square[row][col] = pascal_square[row-1][col-1] + pascal_square[row-1][col]

        # # finalmente, elimino los 0's de relleno
        # pascal_triangle = [
        #     [ elem for elem in row if elem != 0]
        #     for row in pascal_square
        # ]
        
        # # Y devuelvo el rowIndex'th
        # return pascal_triangle[rowIndex]

        # Así, salteando la generacion del triangulo primero
        return [elem for elem in pascal_square[rowIndex] if elem != 0]


# Pruebas
test1 = {'row_index': 3, 'output_exp': [1,3,3,1]}
test2 = {'row_index': 0, 'output_exp': [1]}
test3 = {'row_index': 1, 'output_exp': [1,1]}
tests = [test1]
for test in tests:
    res = Solution().getRow(test['row_index'])
    print('row_index: {} - Resultado esperado: {} - Resultado: {}'.format(test['row_index'], test['output_exp'], res))  
