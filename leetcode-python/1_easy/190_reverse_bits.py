############ LeetCode Problem N° 190: Reverse Bits (Easy) #################
# Reverse bits of a given 32 bits unsigned integer.
# Note:
#   - Note that in some languages, such as Java, there is no unsigned integer type. 
#     In this case, both input and output will be given as a signed integer type. 
#     They should not affect your implementation, as the integer's internal binary 
#     representation is the same, whether it is signed or unsigned.
#   - In Java, the compiler represents the signed integers using 2's complement notation. 
#     Therefore, in Example 2 above, the input represents the signed integer -3 and the 
#     output represents the signed integer -1073741825.
#
# Example 1:
# Input: n = 00000010100101000001111010011100
# Output:    964176192 (00111001011110000010100101000000)
# Explanation: The input binary string 00000010100101000001111010011100 represents the 
# unsigned integer 43261596, so return 964176192 which its binary representation is 00111001011110000010100101000000.
#
# Example 2:
# Input: n = 11111111111111111111111111111101
# Output:   3221225471 (10111111111111111111111111111111)
# Explanation: The input binary string 11111111111111111111111111111101 represents the 
# unsigned integer 4294967293, so return 3221225471 which its binary representation is 10111111111111111111111111111111.
#
# Constraints:
# The input must be a binary string of length 32
#
# Follow up: If this function is called many times, how would you optimize it?

class Solution:
    '''Solución manipulando bits'''
    def reverseBits(self, n: str) -> int:
        '''
        Dado un número entero (de 32 bits), obtiene el reverso del mismo 
        (a partir de su expresión binaria) y devuelve su representación entera.
        
        >>> n = 43261596 (00000010100101000001111010011100)
        >>> reverseBits(n)
        964176192 (00111001011110000010100101000000)
        '''
        reversed = 0
        for i in range(32):
            reversed = reversed << 1
            reversed |= (n >> i) &0x1
        
        return reversed


class SolutionA:
    '''Solución simple Pythonic, empleando métodos: [::-1], int()'''
    def reverseBits(self, n: str) -> int:
        '''
        Dado un número entero (de 32 bits), obtiene el reverso del mismo 
        (a partir de su expresión binaria) y devuelve su representación entera.
        
        >>> n = 43261596 (00000010100101000001111010011100)
        >>> reverseBits(n)
        964176192 (00111001011110000010100101000000)
        '''
        # representación binaria de n, luego reverseo y devuelvo el int
        bin_str = '{0:032b}'.format(n)
        reversed = bin_str[::-1]
        res = int(reversed, 2)
        return res

# Pruebas
test1 = {'n': '00000010100101000001111010011100', 'output_exp': 964176192}
test2 = {'n': 'AB', 'output_exp': 28}
test3 = {'n': 'ZY', 'output_exp': 701}
tests = [test1, test2, test3]
tests = [test1]
for test in tests:
    res = Solution().reverseBits(test['n'])
    print('n: {} - Resultado esperado: {} - Resultado: {}'.format(test['n'], test['output_exp'], res))  