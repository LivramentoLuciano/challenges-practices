######### LeetCode Problem N°2 - Jump Game (Medium) ################
# You are given an integer array nums. You are initially 
# positioned at the array's first index, and each element 
# in the array represents your maximum jump length at that position.
# Return true if you can reach the last index, or false otherwise.
#
# Example 1:
# Input: nums = [2,3,1,1,4]
# Output: true
# Explanation: Jump 1 step from index 0 to 1, then 3 steps to the last index.
#
# Example 2:
# Input: nums = [3,2,1,0,4]
# Output: false
# Explanation: You will always arrive at index 3 no matter what. Its maximum jump length is 0, which makes it impossible to reach the last index.
#
# Constraints:
# 1 <= nums.length <= 104
# 0 <= nums[i] <= 105

class Solution:
    '''Solución backwards'''
    def canJump(self, nums: list[int]) -> bool:
        '''
        Dada una lista de números, sobre la cual comenzaremos
        parándonos en el primer índice, y donde cada elemento
        indica el máximo salto que se puede hacer desde el mismo, 
        devolverá True si es posible alcanzar el final, o False
        caso contrario.

        >>> canJump([2,3,1,1,4])
        True
        '''
        # Algoritmo:
        #   - Comenzando en el ultimo elemento, retrocedo chequeando si el valor nums[i]
        #     permite alcanzar el target, si lo permite, ahora el target pasa a ser ese i
        #     y sigo probando con los elementos anteriores
        #   - Si al terminar, el target está en el primer elemento, quiere decir que hay 
        #     un camino que llega hasta el final
        n = len(nums)
        if n == 1: return True

        target = 1
        for i in range(2, n+1):
            if nums[-i] >= i - target:
                target = i

        return target == n

class SolutionForward:
    def canJump(self, nums: list[int]) -> bool:
        '''
        Dada una lista de números, sobre la cual comenzaremos
        parándonos en el primer índice, y donde cada elemento
        indica el máximo salto que se puede hacer desde el mismo, 
        devolverá True si es posible alcanzar el final, o False
        caso contrario.

        >>> canJump([2,3,1,1,4])
        True
        '''
        # Algoritmo:
        #   - Comenzando en el primer elemento, obtengo el máximo índice 'm'
        #     al que puede llegar
        #   - Repito para cada elemento
        #   - Si uno se encuentra en un index 'i' superior al 'm' quiere decir 
        #     que no podría llegar a este, por tanto, salgo con False
        
        # maximo indice al que puedo llegar desde donde estoy parado
        maxi = 0
        for i, num in enumerate(nums):
            if i > maxi:
                return False
            maxi = max(maxi, i+num)
            
        return True

# Pruebas
test1 = {'nums': [2,3,1,1,4], 'output_exp': True}
test2 = {'nums': [3,2,1,0,4], 'output_exp': False}
test3 = {'nums': [2,0,0], 'output_exp': True}
test4 = {'nums': [1,2,3], 'output_exp': True}
tests = [test1, test2, test3, test4]
# tests = [test4]
for test in tests:
    res = Solution().canJump(test['nums'])
    print('nums: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['output_exp'], res))       

