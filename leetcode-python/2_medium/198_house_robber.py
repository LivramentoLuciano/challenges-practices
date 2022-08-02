######### LeetCode Problem N°198 - House Robber (Medium) ################
# You are a professional robber planning to rob houses along a street. 
# Each house has a certain amount of money stashed, the only constraint 
# stopping you from robbing each of them is that adjacent houses have security 
# systems connected and it will automatically contact the police 
# if two adjacent houses were broken into on the same night.
# Given an integer array nums representing the amount of money of each house, 
# return the maximum amount of money you can rob tonight without alerting the police.
#
# Example 1:
# Input: nums = [1,2,3,1]
# Output: 4
# Explanation: Rob house 1 (money = 1) and then rob house 3 (money = 3).
# Total amount you can rob = 1 + 3 = 4.
#
# Example 2:
# Input: nums = [2,7,9,3,1]
# Output: 12
# Explanation: Rob house 1 (money = 2), rob house 3 (money = 9) and rob house 5 (money = 1).
# Total amount you can rob = 2 + 9 + 1 = 12.
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 400

class Solution:
    def rob(self, nums: list[int]) -> int:
        '''
        Dada una lista "nums" con la cantidad de dinero disponible en cada Casa,
        devuelve la máxima cantidad de dinero que puede robarse de las mismas,
        considerando que no pueden robarse 2 casas aledañas, por un sistema de seguridad        
        '''
        # Algoritmo:
        # Estando en una casa en particular, habrá 2 opciones
        #   - Robar: en este caso, actualizo el 'rob' al último valor de 'not_rob' 
        #            (es decir, sin haber robado la casa previa) + el dinero de la casa en la que estoy
        #   - No Robar: en este caso, se actualiza el 'not_rob' (acumula los montos no robando en cada casa particular)
        #               al máximo entre haber robado o no la casa anterior (rob, not_rob previo)
        rob, not_rob = 0, 0 
        for num in nums:
            rob, not_rob = not_rob + num, max(not_rob, rob)
        
        return max(not_rob, rob)


class SolutionDP:
    def rob(self, nums: list[int]) -> int:
        if not nums: return 0
        n = len(nums)
        dp = [0]*(n+1)
        dp[1] = nums[0]

        for i in range(2, n+1):
            # maximo entre robar esta casa (acumulado con i-2, omite la previa)
            # y el acumulado en la previa
            dp[i] = max(dp[i-2]+nums[i-1], dp[i-1])
            
        return dp[-1]


# Pruebas
test1 = {'nums': [1,2,3,1], 'output_exp': 4}
test2 = {'nums': [2,7,9,3,1], 'output_exp': 12}
test3 = {'nums': [10,1,0,15,1], 'output_exp': 25}
test4 = {'nums': [1,3,1], 'output_exp': 3}
tests = [test1, test2, test3, test4]
for test in tests:
    res = SolutionDP().rob(test['nums'])
    print('Money: {}\tResultado esperado: {}\tResultado: {}'.format(test['nums'], test['output_exp'], res))    
