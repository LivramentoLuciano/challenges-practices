######### LeetCode Problem N°227 - Basic Calculator (Medium) ################
# Given a string s which represents an expression, evaluate this expression 
# and return its value. The integer division should truncate toward zero.
# You may assume that the given expression is always valid. All intermediate 
# results will be in the range of [-231, 231 - 1].
# Note: You are not allowed to use any built-in function which evaluates strings as mathematical expressions, such as eval().
#
# Example 1:
# Input: s = "3+2*2"
# Output: 7
#
# Example 2:
# Input: s = " 3/2 "
# Output: 1
#
# Example 3:
# Input: s = " 3+5 / 2 "
# Output: 5
#
# Constraints:
#   - 1 <= s.length <= 3 * 105
#   - s consists of integers and operators ('+', '-', '*', '/') separated by some number of spaces.
#   - s represents a valid expression.
#   - All the integers in the expression are non-negative integers in the range [0, 231 - 1].
#   - The answer is guaranteed to fit in a 32-bit integer.

class Solution:
    def calculate(self, s: str) -> int:
        print('Calcular:', s)
        # Algoritmo:
        # Recorro la expresión y, al llegar a un signo de operación, guardo en una Pila
        # el número encontrado anterior, en caso de que la última operación sea una suma o resta
        # o bien guardo en la pila el resultado de la multiplicación/división, en caso de que 
        # ese sea el estado de la ultima operación.
        # Luego, actualizo el estado de operación al signo encontrado s[i] y reinicio el número a 0
        # Finalmete, el resultado será la suma de dicha pila
        n = len(s)
        stack, num, op = [], 0, '+'
        for i in range(n):
            if s[i].isdigit(): 
                num = 10*num + int(s[i])

            if (not s[i].isdigit() and s[i] != ' ') or i == n-1:
                if op == '+':
                    stack.append(num)
                elif op == '-':
                    stack.append(-num)
                elif op == '*':
                    stack.append(stack.pop()*num)
                else:
                    stack.append(int(stack.pop()/num))
                
                # Actualizo a la siguiente operación y reseteo num
                op = s[i]
                num = 0
        
        return sum(stack)


import re
class Solution1:
    def calculate(self, s: str) -> int:
        print('Calcular:', s)
        # Algoritmo:
        # Separo primero en terminos de sumas y restas (Outer)
        # Luego, dentro de cada termino, busco las multiplicaciones y divisiones (inner)
        # voy resolviendo las internas, y las sumo/resto al resultado total
        res = 0

        outer = iter(['+'] + re.split('([+-])', s))
        for addsub in outer:
            inner = iter(['*'] + re.split('([*/])', next(outer)))
            term = 1
            for muldiv in inner:
                n = int(next(inner))
                term = term * n if muldiv == '*' else term // n
            res += term if addsub == '+' else -term
        
        return res


# Pruebas
test1={'input': "3+2*2", 'out_exp': 7}
test2={'input': " 3/2 ", 'out_exp': 1}
test3={'input': " 3+5 / 2 ", 'out_exp': 5}
test4={'input': "1-1+1", 'out_exp': 1}
test5={'input': "14-3/2", 'out_exp': 13}
tests = [test1,test2, test3, test4]
tests = [test5]
for test in tests:
    res = Solution().calculate(test['input'])
    print('input: {} - Resultado esperado: {} - Resultado: {}'.format(test['input'], test['out_exp'], res))