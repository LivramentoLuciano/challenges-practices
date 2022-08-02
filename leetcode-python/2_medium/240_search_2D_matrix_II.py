# Write an efficient algorithm that searches for a value target in an  
# m x n integer matrix matrix. This matrix has the following properties:
#   - Integers in each row are sorted in ascending from left to right.
#   - Integers in each column are sorted in ascending from top to bottom.
#
# Example 1:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 5
# Output: true
#
# Example 2:
# Input: matrix = [[1,4,7,11,15],[2,5,8,12,19],[3,6,9,16,22],[10,13,14,17,24],[18,21,23,26,30]], target = 20
# Output: false
#
# Constraints:
#   - m == matrix.length
#   - n == matrix[i].length
#   - 1 <= n, m <= 300
#   - -10**9 <= matrix[i][j] <= 10**9
#   - All the integers in each row are sorted in ascending order.
#   - All the integers in each column are sorted in ascending order.
#   - -10**9 <= target <= 10**9

class Solution:
    '''Solución más rápida. Time: O(m+n)'''
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Algoritmo:
        # Desde bottom-left recorro hacia top-right
        #   - Si el valor mayor a target -> omito esta fila, retrocedo a la anterior (arriba)
        #   - Si el valor menor a target -> avanzo a la siguiente columna
        # Esto es posible por estar ordenada ascending tanto en fila como columna
        m, n = len(matrix), len(matrix[0])

        i, j = m - 1, 0
        while i >= 0 and j < n:
            if matrix[i][j] > target: i -= 1
            elif matrix[i][j] < target: j += 1
            else: return True

        return False


class SolutionBinSearch:
    '''Solución Básica. Time: O(m*log(n))'''
    def searchMatrix(self, matrix: list[list[int]], target: int) -> bool:
        # Algoritmo:
        # Binary Search sobre las distintas filas de la matriz, filtrando
        # a SÓLO aquellas que estén dentro del rango del target
        n = len(matrix[0])
        for row in matrix:
            if (row[0] <= target <= row[n-1]) and self.searchRow(row, target):
                return True
        return False

    def searchRow(self, row: list[int], target: int) -> bool:
        '''Binary Search de Target sobre una Lista (fila de la matriz)'''
        l, h = 0, len(row) - 1
        while l <= h:
            center = (l + h) // 2
            value = row[center]
            if value < target: l = center + 1
            elif value > target: h = center - 1
            else: return True
        return False

# Pruebas
test1 = {
    'matrix': [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ],
    'target': 5, 
    'output_exp': True
}
test2 = {
    'matrix': [
        [1,4,7,11,15],
        [2,5,8,12,19],
        [3,6,9,16,22],
        [10,13,14,17,24],
        [18,21,23,26,30]
    ],
    'target': 20, 
    'output_exp': False
}
tests = [test1, test2]
tests = [test1]
for test in tests:
    res = Solution().searchMatrix(test['matrix'], test['target'])
    print('Matriz:')
    for row in test['matrix']: print(row)
    print('target: {}'.format(test['target']))
    print('Resultado esperado: {} - Resultado: {}'.format(test['output_exp'], res))
    print('='*100)
