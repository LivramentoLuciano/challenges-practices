############ LeetCode Problem N° 136: Single Number (Easy) #################
# Given a non-empty array of integers nums, every element 
# appears twice except for one. Find that single one.
# You must implement a solution with a linear runtime complexity 
# and use only constant extra space.
#
# Example 1:
# Input: nums = [2,2,1]
# Output: 1
#
# Example 2:
# Input: nums = [4,1,2,1,2]
# Output: 4
#
# Example 3:
# Input: nums = [1]
# Output: 1
#
# Constraints:
# 1 <= nums.length <= 3 * 104
# -3 * 104 <= nums[i] <= 3 * 104
# Each element in the array appears twice except for one element which appears only once.
from functools import reduce

class SolutionXOR2:
    '''Solución basada en XOR, SÍ cumple Space: O(1). Variante utilizando reduce.'''
    def singleNumber(self, nums: list[int]) -> int:
        '''
        Dado un array de numeros, donde todos menos uno 
        están repetidos una vez. Devuelve ese único número
        que no está repetido.
        >>> singleNumber([4,1,2,1,2])
        4
        '''
        # Fundamento funcionamiento:
        # a XOR 0 = a ---- a XOR a = 0 ---- XOR es asociativa
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b 
        # => a XOR b XOR a = b
        # Conclusión: si realizamos una XOR de todos los elementos de nums, 
        # obtendremos como resultado el único elemento no repetido
        #
        # Aplicando reduce(fn,seq)
        # Usando lambda u operator.xor
        return reduce(lambda a,b: a^b, nums)
        return reduce(operator.xor, nums)
        
class SolutionXOR:
    '''Solución basada en XOR, SÍ cumple Space: O(1)'''
    def singleNumber(self, nums: list[int]) -> int:
        '''
        Dado un array de numeros, donde todos menos uno 
        están repetidos una vez. Devuelve ese único número
        que no está repetido.
        >>> singleNumber([4,1,2,1,2])
        4
        '''
        # Fundamento funcionamiento:
        # a XOR 0 = a ---- a XOR a = 0 ---- XOR es asociativa
        # a XOR b XOR a = (a XOR a) XOR b = 0 XOR b 
        # => a XOR b XOR a = b
        # Conclusión: si realizamos una XOR de todos los elementos de nums, 
        # obtendremos como resultado el único elemento no repetido
        res = 0
        for num in nums:
            res ^= num

        return res

class SolutionSum:
    '''Solución inicial, basada en sumatoria, no cumple Space: O(1)'''
    def singleNumber(self, nums: list[int]) -> int:
        '''
        Dado un array de numeros, donde todos menos uno 
        están repetidos una vez. Devuelve ese único número
        que no está repetido.
        >>> singleNumber([4,1,2,1,2])
        4
        '''
        # Fundamento del algoritmo:
        # Siendo nums: [1,1,2,2,3,3,4]
        # El set de nums: [1,2,3,4]
        # Si definimos al numero unico X (incognita)
        # SUM(nums) + X = 2*SUM(set_nums)
        return 2*sum(set(nums)) - sum(nums)
                
class SolutionCounter:
    '''Solución inicial, basada en contador de numeros, NO cumple Space: O(1)'''
    def singleNumber(self, nums: list[int]) -> int:
        '''
        Dado un array de numeros, donde todos menos uno 
        están repetidos una vez. Devuelve ese único número
        que no está repetido.
        >>> singleNumber([4,1,2,1,2])
        4
        '''
        counter = {}
        for num in nums:
            counter[num] = counter.get(num, 0) + 1

        for key, value in counter.items():
            if value == 1:
                return key


# Pruebas
test1 = {'nums': [2,2,1], 'output_exp': 1}
test2 = {'nums': [4,1,2,1,2], 'output_exp': 4}
tests = [test1, test2]
for test in tests:
    res = SolutionXOR2().singleNumber(test['nums'])
    print('nums: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['output_exp'], res))