# Given two binary strings a and b, return their sum as a binary string.
#
# Example 1:
# Input: a = "11", b = "1"
# Output: "100"
#
# Example 2:
# Input: a = "1010", b = "1011"
# Output: "10101"
#
# Constraints:
# 1 <= a.length, b.length <= 104
# a and b consist only of '0' or '1' characters.
# Each string does not contain leading zeros except for the zero itself.

class Solution_BuiltIn:
    '''
    Solución utilizando métodos buil-in de Python para el procesamiento
    de números binarios    
    '''
    def addBinary(self, a: str, b: str) -> str:
        # Obtengo los numeros binarios indicados por los strings
        # Nota: Python los procesa y muestra en su representación decimal
        bin1 = int(a,2)
        bin2 = int(b,2)
        bin_sum = bin1 + bin2

        # bin(num) -> devuelve un str con la representación binaria
        # del numero ('0bxxx'), sino Python muestra base decimal
        # print(f'{bin(bin1)} + {bin(bin2)} = {bin(bin_sum)}')
        bin_sum = bin(bin_sum)

        # ... luego remuevo el indicador '0b' y listo!
        res = bin_sum.split('0b')[1]

        return res

class Solution:
    '''Solución mediante la suma binaria pura y recursividad'''
    def addBinary(self, a: str, b: str) -> str:
        # Mecanica, suma los el último bit de cada numero binario (string)
        # Entonces si:
        #   - 1+1 -> resultado: un '0' y a la izquierda sumar lo restante de
        #                       a y b, y a ese resultado sumarle 1 (carry)  
        #   - 0+0 -> resultado: un '0' y a su izquierda sumar lo restante de
        #                       a y b (sin carry) 
        #   - 1+0, 0+1 -> resultado: un '1' y a su izquierda sumar lo restante 
        #                            de a y b (sin carry)

        # Si uno de los binary strings llega vacio 
        # la suma será directamente el otro
        # (Si uno tiene mas bits, al aplicar recursividad se dara
        #  que llegara un momento que querra sumar '11' + '', p/ej)
        if len(a)==0: return b
        if len(b)==0: return a 
              
        if a[-1]=='1' and b[-1]=='1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), '1') + '0'
        elif a[-1]=='0' and b[-1]=='0':
            return self.addBinary(a[:-1], b[:-1]) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + '1'


class Solution_b:
    '''Solución mediante la suma binaria pura y recursividad'''
    def add_bit(self, b1:str, b2:str) ->tuple:
        '''Dados 2 bits (en caracter), realiza su suma binaria, indicando si hay carry'''
        res = '1' if (b1=='1' and b2=='0') or (b1=='0' and b2=='1') else '0'
        carry = '1' if (b1=='1' and b2=='1') else '0'
        return (res, carry)

    def addBinary(self, a: str, b: str) -> str:
        if len(a) == 0: return b
        if len(b) == 0: return a

        res, carry = self.add_bit(a[-1], b[-1])
        
        if carry == '1':
            return self.addBinary(self.addBinary(a[:-1], b[:-1]), carry) + '0'
        else:
            return self.addBinary(a[:-1], b[:-1]) + res

# Pruebas
test1 = {'num1': '11', 'num2': '1', 'output_exp':'100'}
test2 = {'num1': '11', 'num2': '11', 'output_exp':'110'}
test3 = {'num1': '1010', 'num2': '1011', 'output_exp':'10101'}
test4 = {'num1': '', 'num2': '', 'output_exp':''}
tests = [test1, test2 ,test3, test4]

for test in tests:
    res = Solution_b().addBinary(test['num1'], test['num2'])
    print(test['num1'],'+', test['num2'],' = ', res, ' - Resultado esperado:', test['output_exp'])
