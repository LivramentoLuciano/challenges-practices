######### LeetCode Problem N°1 - Two sum (Easy) ################
# Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.
# You may assume that each input would have exactly one solution, and you may not use the same element twice.
# You can return the answer in any order.
#
# Example;
# Input: nums = [2,7,11,15], target = 9
# Output: [0,1]
# Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].
#
# Constraints:
# 2 <= nums.length <= 104
# -109 <= nums[i] <= 109
# -109 <= target <= 109
# Only one valid answer exists.

class Solution:
    ''' Solucción adecuada (más veloz) empleando Diccionario (hash) de valores vistos '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Indices de los números ya vistos
        seen = {}
        for i, num in enumerate(nums):
            remaining = target - num

            if remaining in seen:
                return [seen[remaining], i]
            else:
                seen[num] = i

class SolutionA:
    ''' Solución Inicial '''
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Tomo numeros de izq a derecha (hasta anteultimo)
        # sumandole c/u de los de la derecha
        for i, num1 in enumerate(nums[:-1]):
            for j, num2 in enumerate(nums[i+1:]):
                if num1 + num2 == target:
                    return [i, j+(i+1)]
        
        # Dice que asumamos que hay una solucion (unica)
        # pero por las dudas... si no encontro solucion -> []
        return []

# pruebas
test1 = {'nums': [2,7,11,15], 'target': 9, 'output_exp': [0,1]}
tests = [test1]
for test in tests:
    res = Solution().twoSum(test['nums'], test['target'])
    print('nums: {}, target: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['target'], test['output_exp'], res))  
