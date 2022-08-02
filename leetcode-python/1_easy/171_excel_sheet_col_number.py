############ LeetCode Problem N° 171: Excel Sheet Column Number (Easy) #################
# Given a string columnTitle that represents the column title 
# as appears in an Excel sheet, return its corresponding column number.
# For example:
# A -> 1
# B -> 2
# C -> 3
# ...
# Z -> 26
# AA -> 27
# AB -> 28 
# ...
#
# Example 1:
# Input: columnTitle = "A"
# Output: 1
#
# Example 2:
# Input: columnTitle = "AB"
# Output: 28
#
# Example 3:
# Input: columnTitle = "ZY"
# Output: 701
#
# Constraints:
# 1 <= columnTitle.length <= 7
# columnTitle consists only of uppercase English letters.
# columnTitle is in the range ["A", "FXSHRXW"].

class Solution:
    '''Solución sin diccionario, empleando Ord para obtener el valor de cada caracter'''
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        Dado el Nombre de una Columna como aparece en una
        Hoja de Excel (A, B, C, ..., AA, AB, ...), devuelve
        el número representativo de la misma.
        >>> titleToNumber(A)
        1
        >>> titleToNumber(Z)
        26
        >>> titleToNumber(AB)
        28
        '''
        # Algoritmo
        # Se realiza la construcción del valor de igual manera que con un número 
        # decimal, sólo que en este caso los dígitos son A, B...Z y su base será 26
        res = 0
        for l in columnTitle:
            res = res*26 + (ord(l) - ord('A') + 1)
        return res


import string
class SolutionA:
    '''Solución empleando un Dict de conversión de Caracter a Int'''
    def titleToNumber(self, columnTitle: str) -> int:
        '''
        Dado el Nombre de una Columna como aparece en una
        Hoja de Excel (A, B, C, ..., AA, AB, ...), devuelve
        el número representativo de la misma.
        >>> titleToNumber(A)
        1
        >>> titleToNumber(Z)
        26
        >>> titleToNumber(AB)
        28
        '''
        # Algoritmo
        # Se realiza la construcción del valor de igual manera que con un número 
        # decimal, sólo que en este caso los dígitos son A, B...Z y su base será 26
        LETTER_VAL = { letter: i+1 for i,letter in enumerate(string.ascii_uppercase)}
        res = 0
        for l in columnTitle:
            res = res*26 + LETTER_VAL[l]
        return res
    
# Pruebas
test1 = {'columnTitle': 'A', 'output_exp': 1}
test2 = {'columnTitle': 'AB', 'output_exp': 28}
test3 = {'columnTitle': 'ZY', 'output_exp': 701}
tests = [test1, test2, test3]
for test in tests:
    res = Solution().titleToNumber(test['columnTitle'])
    print('columnTitle: {} - Resultado esperado: {} - Resultado: {}'.format(test['columnTitle'], test['output_exp'], res))    