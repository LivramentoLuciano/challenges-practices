############ LeetCode Problem N° 7: Reverse Integer (Medium) #################
# Given a signed 32-bit integer x, return x with its digits reversed. 
# If reversing x causes the value to go outside the signed 32-bit integer 
# range [-2**31, 2**31 - 1], then return 0.
# Assume the environment does not allow you to store 64-bit integers (signed or unsigned).
#
# Example 1:
# Input: x = 123
# Output: 321
#
# Example 2:
# Input: x = -123
# Output: -321
#
# Example 3:
# Input: x = 120
# Output: 21
#
# Constraints:
# -231 <= x <= 231 - 1
class Solution:
    def reverse(self, x: int) -> int:
        # convierto a str el num, lo doy vuelta y vuelvo a int
        sign = -1 if x<0 else 1
        x_str = str(abs(x))

        if -(2**31) <= sign * int(x_str[::-1]) < 2**31: 
            return sign * int(x_str[::-1])
        else: 
            return 0

class Solution2:
    '''Sin utilizar métodos str'''
    def reverse(self, x: int) -> int:       
        sign = -1 if x < 0 else 1
        x = abs(x)
        res = 0

        # voy obteniendo los digitos inversos (con el % 10)
        while x:
            res = res * 10 + x % 10
            x = x // 10
        
        if -(2**31) <= sign*res < 2**32: 
            return sign*res
        else:
            return 0


# Pruebas
test1 = {'n': 123, 'output_exp': 321}
test2 = {'n': -123, 'output_exp': -321}
test3 = {'n': 120, 'output_exp': 21}
test4 = {'n': 0, 'output_exp': 0}
tests = [test4]
for test in tests:
    res = Solution().reverse(test['n'])
    print('n: {} - Resultado esperado: {} - Resultado: {}'\
        .format(test['n'], test['output_exp'], res))    
