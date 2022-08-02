############ LeetCode Problem N° 13: Pascal´s Triangle (Easy) #################
# Given an integer numRows, return the first numRows of Pascal's triangle.
# In Pascal's triangle, each number is the sum of the two numbers directly above it as shown:
#
# Example 1:
# Input: numRows = 5
# Output: [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
#
# Example 2:
# Input: numRows = 1
# Output: [[1]]
#
# Constraints:
# 1 <= numRows <= 30

class Solution:
    def generate(self, numRows: int) -> list[list[int]]:
        '''
        Dada una cantidad de filas "numRows" devuelve dicha cantidad
        de filas del comienzo del Triángulo de Pascal.

        >>> generate(5)
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        '''
        # Sin necesidad de usar un cuadrado de base, inicializo con 1's
        triangle = [[1]*(i+1) for i in range(numRows)]

        for row in range(numRows):
            for col in range(1, row):
                triangle[row][col] = triangle[row-1][col-1] + triangle[row-1][col]

        return triangle


class SolutionA:
    def generate(self, numRows: int) -> list[list[int]]:
        '''
        Dada una cantidad de filas "numRows" devuelve dicha cantidad
        de filas del comienzo del Triángulo de Pascal.

        >>> generate(5)
        [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]
        '''
        # Tomo de base un Cuadrado (relleno con 0´s). 
        # Luego, devuelvo solo el triangulo.
        # [[0]*(numRows+1)]*numRows # Falla, por referencias al modificar lista
        square = [[0]*(numRows+1) for _ in range(numRows)]
        square[0][1] = 1

        for row in range(1, numRows):
            for col in range(1, row+2):
                square[row][col] = square[row-1][col-1] + square[row-1][col]

        return [
            square[i][1:i+2]
            for i in range(len(square))
        ]

# Pruebas
test1 = {'num_rows': 5, 'output_exp': [[1],[1,1],[1,2,1],[1,3,3,1],[1,4,6,4,1]]}
test2 = {'num_rows': 1, 'output_exp': [[1]]}
tests = [test1]
for test in tests:
    res = Solution().generate(test['num_rows'])
    print('num_rows: {} - Resultado esperado: {} - Resultado: {}'.format(test['num_rows'], test['output_exp'], res))  
