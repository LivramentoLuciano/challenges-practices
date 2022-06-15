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


# Resultados:
# Runtime: 5167 ms, faster than 15.99% 
# Memory Usage: 15 MB, less than 76.39%
# 
# TODO: Pruebas para mejorar la velocidad
