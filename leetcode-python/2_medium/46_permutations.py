########## LeetCode Problem N°36 - Permutations (Medium) ################
# Given an array nums of distinct integers, return all the possible permutations. 
# You can return the answer in any order.
#
# Example 1:
# Input: nums = [1,2,3]
# Output: [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
#
# Example 2:
# Input: nums = [0,1]
# Output: [[0,1],[1,0]]
#
# Example 3:
# Input: nums = [1]
# Output: [[1]]
#
# Constraints:
# 1 <= nums.length <= 6
# -10 <= nums[i] <= 10
# All the integers of nums are unique.

class Solution:
    '''Solución Aplicando recursividad'''
    def permute(self, nums: list[int]) -> list[list[int]]:
        '''
        Dado un array de números, devuelve todas las posibles
        permutaciones del mismo, es decir, variantes de ordenar 
        los elementos de maneras distintas.

        >>> permute([1,2,3])
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        '''
        # Resolución: 
        # Cada permutación resulta de incrustar el primer caracter
        # en todas las posiciones dentro de las permutaciones posibles
        # del resto de la lista
        # Ejemplo: [1,2,3] -> incrustar el 1, dentro de las permutaciones de [2,3] = [2,3], [3,2]
        # Entonces -> [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
        # print(self.incrust_num(nums[0], [nums[1:]]))

        # Aplicando Recursividad
        # casos base
        if not nums: return []
        if len(nums) == 1: return [nums]

        return self.incrust_num(nums[0], self.permute(nums[1:]))

    def incrust_num(self, num:int, nums:list[list[int]]) -> list[list[int]]:
        '''
        Función helper, incrusta un número en todas las posiciones 
        posibles dentro de una lista de listas de numeros (permutaciones)
        '''
        incrustations = []
        for a_nums in nums:
            a_incrustations = []
            for i in range(len(a_nums)+1):
                inc = list(a_nums)
                inc.insert(i, num)
                a_incrustations.append(inc)
            incrustations.extend(a_incrustations)
        
        return incrustations
            

class SolutionDP:
    '''Solución Aplicando Dynamic Programming'''
    def permute(self, nums: list[int]) -> list[list[int]]:
        '''
        Dado un array de números, devuelve todas las posibles
        permutaciones del mismo, es decir, variantes de ordenar 
        los elementos de maneras distintas.

        >>> permute([1,2,3])
        [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]
        '''
        # Resolución: 
        # Cada permutación resulta de incrustar el primer caracter
        # en todas las posiciones dentro de las permutaciones posibles
        # del resto de la lista
        # Ejemplo: [1,2,3] -> incrustar el 1, dentro de las permutaciones de [2,3] = [2,3], [3,2]
        # Entonces -> [[1,2,3],[2,1,3],[2,3,1],[1,3,2],[3,1,2],[3,2,1]]
        # print(self.incrust_num(nums[0], [nums[1:]]))
        n = len(nums)

        # dp[i] -> permutaciones para nums[-i]
        # casos base
        dp = [None]*(n+1)
        dp[1] = [[nums[-1]]]

        for i in range(2, n+1):
            dp[i] = self.incrust_num(nums[-i], dp[i-1])
        
        return dp[n]

    def incrust_num(self, num:int, nums:list[list[int]]) -> list[list[int]]:
        '''
        Función helper, incrusta un número en todas las posiciones 
        posibles dentro de una lista de listas de numeros (permutaciones)
        '''
        incrustations = []
        for a_nums in nums:
            a_incrustations = []
            for i in range(len(a_nums)+1):
                inc = list(a_nums)
                inc.insert(i, num)
                a_incrustations.append(inc)
            incrustations.extend(a_incrustations)
        
        return incrustations        

# Pruebas
test1 = {'nums': [1,2,3], 'output_exp': [[1,2,3],[1,3,2],[2,1,3],[2,3,1],[3,1,2],[3,2,1]]}
test2 = {'nums': [0,1], 'output_exp': [[0,1],[1,0]]}
tests = [test1, test2]
for test in tests:
    res = SolutionDP().permute(test['nums'])
    print('nums: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['output_exp'], res))       
