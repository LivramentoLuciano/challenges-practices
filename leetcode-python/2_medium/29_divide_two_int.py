######### LeetCode Problem N°29 - Divide Two Integers (Medium) ################
# Given two integers dividend and divisor, divide two integers without using 
# multiplication, division, and mod operator. The integer division should 
# truncate toward zero, which means losing its fractional part. For example, 8.345 
# would be truncated to 8, and -2.7335 would be truncated to -2.
#
# Return the quotient after dividing dividend by divisor.
# Note: Assume we are dealing with an environment that could only store 
# integers within the 32-bit signed integer range: [−231, 231 − 1]. For this problem,
#  if the quotient is strictly greater than 231 - 1, then return 231 - 1, and if the 
# quotient is strictly less than -231, then return -231.
#
# Example 1:
# Input: dividend = 10, divisor = 3
# Output: 3
# Explanation: 10/3 = 3.33333.. which is truncated to 3.
#
# Example 2:
# Input: dividend = 7, divisor = -3
# Output: -2
# Explanation: 7/-3 = -2.33333.. which is truncated to -2.
#
# Constraints:
# -231 <= dividend, divisor <= 231 - 1
# divisor != 0

class Solution1:
    def __init__(self):
        self.MAX_POSITIVE = (2**31)-1
        self.MAX_NEGATIVE = -(2**31)

    def multiply(self, n1:int, n2:int) ->int:
        '''Realiza una multiplicación sin utilizar /, * ni mod'''
        res = 0
        # n2 el menor y n1 el mayor, evita loops enormes (2**32)
        if n2>n1: n1, n2 =  n2, n1

        for i in range(n2):
            # si el resultado va a superar el lim de 32bits, devuelvo overflow
            if res+n1 > self.MAX_POSITIVE+1:
                return -1
            res += n1
        return res

    def divide(self, dividend: int, divisor: int) -> int:
        '''Realiza una división sin utilizar /, * ni mod'''
        # Casos extremos: 
        # - limite 32 bits 
        #   - Si se que dará > max_positive no puedo almacenarlo
        #   - Si se que dará max_negative no puedo calcularlo (search) xq supera el limite positivo  
        # - max_positive no podria hallarlo con search binario xq esta en el limite justo
        if dividend == self.MAX_NEGATIVE and divisor == -1: return self.MAX_POSITIVE
        if dividend == self.MAX_NEGATIVE and divisor == 1: return self.MAX_NEGATIVE
        if dividend == self.MAX_POSITIVE and divisor == 1: return self.MAX_POSITIVE

        # Binary Search del numero que al multiplicar por 'divisor'
        # me de el dividendo (dividendo-divisor < res <= dividendo)
        #
        # proceso como si fueran positivos, luego aplico el signo al resultado
        res_positive = not ((dividend>0) ^ (divisor>0))
        dividend, divisor = abs(dividend), abs(divisor)

        left = -1
        right = self.MAX_POSITIVE
        center = (right + left) // 2
        
        i=0
        while True:
            # avoid infinite loops
            if i > 1000: break
            mult = self.multiply(center, divisor)
            # print('Left:', left, 'Right:', right, 'Center:', center, 'mult:', mult)

            # catch overflow en la multiplicacion
            if mult == -1: 
                right = center
                center = (right + left) // 2                
            
            elif  mult > (dividend - divisor) and mult <= dividend:
                # Center es el resultado de la division (trunqueado)
                res = center if res_positive else -center
                return res
            elif mult > dividend:
                right = center
                center = (right + left) // 2
            else:
                left = center
                center = (right + left) // 2
                
            i += 1
        return None


class Solution:
    def __init__(self):
        self.MAX_POSITIVE = (2**31)-1
        self.MAX_NEGATIVE = -(2**31)

    def divide(self, dividend: int, divisor: int) -> int:
        '''Realiza una división sin utilizar /, * ni mod'''
        # Casos extremos: 
        # - limite 32 bits 
        #   - Si se que dará > max_positive no puedo almacenarlo
        #   - Si se que dará max_negative no puedo calcularlo (search) xq supera el limite positivo  
        # - max_positive no podria hallarlo con search binario xq esta en el limite justo
        if dividend == self.MAX_NEGATIVE and divisor == -1: return self.MAX_POSITIVE
        if dividend == self.MAX_NEGATIVE and divisor == 1: return self.MAX_NEGATIVE
        if dividend == self.MAX_POSITIVE and divisor == 1: return self.MAX_POSITIVE

        # proceso como si fueran positivos, luego aplico el signo al resultado
        positive = not ((dividend>0) ^ (divisor>0))
        dividend, divisor = abs(dividend), abs(divisor)
        
        res = 0
        aux_sum = divisor

        while divisor <= dividend:
            current_res = 1
            
            while (aux_sum + aux_sum) <= dividend:
                aux_sum += aux_sum
                current_res += current_res
            
            dividend -= aux_sum    
            aux_sum = divisor
            res += current_res  

        if not positive: res = -res

        # min(max(-2147483648,res),2147483647)
        return res


test1 = {
    'dividend': 7, 
    'divisor':-3, 
    'output_exp': -2
}    
# Prueba 32 bits (no puede mostrar +2**32)
test2 = {
    'dividend': -2147483648, 
    'divisor': -1, 
    'output_exp': 2147483647
} 
test3 = {
    'dividend': 2147483647, 
    'divisor': 1, 
    'output_exp': 2147483647
}
test4 = {
    'dividend': 1004958205, 
    'divisor': -2137325331, 
    'output_exp': 0
} 
test5 = {
    'dividend': -1021989372, 
    'divisor': -82778243, 
    'output_exp': 12
}
test6 = {
    'dividend': -2147483648, 
    'divisor': 2, 
    'output_exp': -1073741824
}

tests = [test1, test2, test3, test4, test5, test6]
# tests = [test6]
for test in tests:
    res = Solution().divide(test['dividend'], test['divisor'])
    print('{} / {} Resultado esperado: {} Resultado: {}'\
        .format(test['dividend'], test['divisor'], test['output_exp'], res))
