######### LeetCode Problem N°79 - Word Search (Medium) ################
# Given an m x n grid of characters board and a string word, 
# return true if word exists in the grid.
# The word can be constructed from letters of sequentially adjacent cells, 
# where adjacent cells are horizontally or vertically neighboring. 
# The same letter cell may not be used more than once.
#
# Example 1:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCCED"
# Output: true
#
# Example 2:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "SEE"
# Output: true
#
# Example 3:
# Input: board = [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], word = "ABCB"
# Output: false
#
# Constraints:
# m = board.length
# n = board[i].length
# 1 <= m, n <= 6
# 1 <= word.length <= 15
# board and word consists of only lowercase and uppercase English letters.
#
# Follow up: Could you use search pruning to make your solution faster with a larger board?

# TODO: Precheck(), caracteres de la palabra existan en la tabla (mejora rendimiento)
# Comentario: 'k' evita aplicar slice en cada recursividad (mejora rendimiento)
class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        '''
        Busca una palabra dentro de una tabla, formada a través de los vecinos (ltrb).
        '''
        # Busco la palabra, iniciando en cada posible letra de la tabla
        for i in range(len(board)):
            for j in range(len(board[0])):
                # si en algún intento encuentra la palabra, sale Ok
                if self.dfs(board, i, j, word, 0):
                    return True
        return False

    def dfs(self, board, i, j, search, k):
        '''Recorro el board, verifico si encontro la palabra en el camino'''
        # Condición de salida Ok
        # Chequeó todos los caracteres de la palabra target
        if k == len(search): return True

        # Si la letra de la palabra y la actual de la board no coinciden, sale False
        # Filtro condiciones de fallo
        if i<0 or j<0 or i>=len(board) or j>=len(board[0]) or search[k] != board[i][j]:
            return False
        
        # marco visitado temporalmente y continuo buscando el resto de la palabra
        board[i][j] = '#'
        k += 1

        res = self.dfs(board, i-1, j, search, k) or self.dfs(board, i+1, j, search, k) or \
              self.dfs(board, i, j-1, search, k) or self.dfs(board, i, j+1, search, k)
              
        # restauro el valor del casillero marcado anteriormente
        board[i][j] = search[k-1]
        return res

# Pruebas
test1={'board': [["A","B","C","E"],["S","F","C","S"],["A","d","E","E"]], 'word':'ABCCED', 'out_exp': True}
test2={'board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'word':'SEE', 'out_exp': True}
test3={'board': [["A","B","C","E"],["S","F","C","S"],["A","D","E","E"]], 'word':'ASX', 'out_exp': False}
tests = [test1,test2, test3]

for test in tests:
    res = Solution().exist(test['board'], test['word'])
    print('board:', test['board'], 'word', test['word'], 'Resultado esperado:', test['out_exp'], 'Resultado:', res)