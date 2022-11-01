############ LeetCode Problem N° 168: Excel Sheet Column Title (Easy) #################
# Given an integer columnNumber, return its corresponding column title as it appears in an Excel sheet.
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
# Input: columnNumber = 1
# Output: "A"
#
# Example 2:
# Input: columnNumber = 28
# Output: "AB"
#
# Example 3:
# Input: columnNumber = 701
# Output: "ZY"
# 
# Constraints:
# 1 <= columnNumber <= 231 - 1
import string
class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        # 28 = 1*26**1 + 2*26**0 => map(1)='A', map(2)='B' => 28 = 'AB'
        NUM_TO_LETTER = { i:l for i,l in enumerate(string.ascii_uppercase) } 
        
        # Obtengo cada letra, dividiendo sucesivamente por el modulo 26 
        # (análogo a unids, decenas, centenas)
        col_letters = []
        while columnNumber > 0:
            resto = (columnNumber-1) % 26
            col_letters.append(NUM_TO_LETTER[resto])
            columnNumber = (columnNumber-1) // 26 

        # reordeno las letras por peso (ya que se obtuvieron de menor a mayor)
        col_letters = col_letters[::-1]        

        # Y lo devuelvo como un string
        return ''.join(col_letters)
    
# Pruebas
test1 = {'columnNumber': 1, 'output_exp': 'A'}
test2 = {'columnNumber': 28, 'output_exp': 'AB'}
test3 = {'columnNumber': 701, 'output_exp': "ZY"}
test4 = {'columnNumber': 52, 'output_exp': "AZ"}
# tests = [test1, test2, test3]
tests = [test4]
for test in tests:
    res = Solution().convertToTitle(test['columnNumber'])
    print('columnNumber: {} - Resultado esperado: {} - Resultado: {}'.format(test['columnNumber'], test['output_exp'], res))    