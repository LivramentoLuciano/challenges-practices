######### LeetCode Problem N°54 - Spiral Matrix (Medium) ################
# Given an m x n matrix, return all elements of the matrix in spiral order.
#
# Example 1:
# Input: matrix = [[1,2,3],[4,5,6],[7,8,9]]
# Output: [1,2,3,6,9,8,7,4,5]
#
# Example 2:
# Input: matrix = [[1,2,3,4],[5,6,7,8],[9,10,11,12]]
# Output: [1,2,3,4,8,12,11,10,9,5,6,7]
#
# Constraints:
# - m == matrix.length
# - n == matrix[i].length
# - 1 <= m, n <= 10
# - -100 <= matrix[i][j] <= 100

class Solution2:
    # de manera recursiva, voy extrayendo: 
    # - fila superior
    # - columna derecha
    # - fila inferior
    # - columna izquierda        
    def helper(self, matrix, res):
        if not matrix: return

        # try -> Por si intenta hacer pop() habiéndose siendo que ya no hay mas matrix
        try:
            res += matrix.pop(0)                    # top row
            res += [r.pop() for r in matrix]        # right col
            res += matrix.pop()[::-1]               # bottom row (orden inverso)
            res += [r.pop(0) for r in matrix][::-1] # left col (orden inverso)
            self.helper(matrix, res)
        except:
            return
        
    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        matrix_c = [r[:] for r in matrix]
        res = []
        self.helper(matrix_c, res)
        return res

RIGHT = 'r'
DOWN = 'd'
LEFT = 'l'
UP = 'u'
class Solution:
    def __init__(self):
        self.i = 0
        self.j = 0
        self.direction = RIGHT

    def spiralOrder(self, matrix: list[list[int]]) -> list[int]:
        matrix_copy = [r[:] for r in matrix[:]]
        m, n = len(matrix_copy), len(matrix_copy[0])
        res = []

        def can_move(i, j):
            for ii, jj in [(i, j-1), (i-1, j), (i, j+1), (i+1, j)]:
                if 0 <= ii < m and 0 <= jj < n and matrix_copy[ii][jj] != "#":
                    return True
            return False

        def can_move_forward(i, j):
            if self.direction == RIGHT: return j < n-1 and matrix_copy[i][j+1] != "#"
            elif self.direction == DOWN: return i < m-1 and matrix_copy[i+1][j] != "#"
            elif self.direction == LEFT: return j > 0 and matrix_copy[i][j-1] != "#"
            else: return i > 0 and matrix_copy[i-1][j] != "#"
        
        def move_forward():            
            if self.direction == RIGHT: self.j += 1
            elif self.direction == DOWN: self.i += 1
            elif self.direction == LEFT: self.j -= 1
            else: self.i -= 1   

        def change_direction():            
            if self.direction == RIGHT: self.direction = DOWN
            elif self.direction == DOWN: self.direction = LEFT
            elif self.direction == LEFT: self.direction = UP
            else: self.direction = RIGHT                
                        
        while True:
            # visito el elemento y me muevo en la dirección permitida, 
            # respetando el orden de la espiral (right, down, left, top)            
            res.append(matrix_copy[self.i][self.j])
            matrix_copy[self.i][self.j] = "#"
            
            if can_move_forward(self.i, self.j):                 
                move_forward()
            elif can_move(self.i, self.j):                 
                change_direction()
                move_forward()
            else: break

        return res


# Pruebas
test1 = {'matrix': [[1,2,3],[4,5,6],[7,8,9]], 'output_exp': [1,2,3,6,9,8,7,4,5]}
test2 = {'matrix': [[1,2,3,4],[5,6,7,8],[9,10,11,12]], 'output_exp': [1,2,3,4,8,12,11,10,9,5,6,7]}
test3 = {'matrix': [[1,2,3,4],[5,6,7,8],[9,10,11,12],[13,14,15,16]], 'output_exp': [1,2,3,4,8,12,16,15,14,13,9,5,6,7,11,10]}
tests = [test1, test2]
tests = [test1]
for test in tests:
    res = Solution2().spiralOrder(test['matrix'])
    print('matrix: {} - Resultado esperado: {} - Resultado: {}'.format(test['matrix'], test['output_exp'], res))
