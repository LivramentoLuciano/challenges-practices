######### LeetCode Problem N°167 - TWo Sum II (Medium) ################
# Given a 1-indexed array of integers numbers that is already sorted 
# in non-decreasing order, find two numbers such that they add up to a 
# specific target number. Let these two numbers be numbers[index1] and 
# numbers[index2] where 1 <= index1 < index2 <= numbers.length.
# Return the indices of the two numbers, index1 and index2, added by 
# one as an integer array [index1, index2] of length 2.
#
# The tests are generated such that there is exactly one solution. You may not use the same element twice.
# Your solution must use only constant extra space.
#
# Example 1:
# Input: numbers = [2,7,11,15], target = 9
# Output: [1,2]
# Explanation: The sum of 2 and 7 is 9. Therefore, index1 = 1, index2 = 2. We return [1, 2].
#
# Example 2:
# Input: numbers = [2,3,4], target = 6
# Output: [1,3]
# Explanation: The sum of 2 and 4 is 6. Therefore index1 = 1, index2 = 3. We return [1, 3].
#
# Example 3:
# Input: numbers = [-1,0], target = -1
# Output: [1,2]
# Explanation: The sum of -1 and 0 is -1. Therefore index1 = 1, index2 = 2. We return [1, 2].
#
# Constraints:
# 2 <= numbers.length <= 3 * 104
# -1000 <= numbers[i] <= 1000
# numbers is sorted in non-decreasing order.
# -1000 <= target <= 1000
# The tests are generated such that there is exactly one solution.

class Solution:
    '''Solución mediante punteros'''
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        '''
        Dada una lista de números ordenados (asdending) y un target, devuelve
        un array con los índices (1-index) de los 2 números que suman dicho objetivo.

        >>> twoSum([2,3,4], 6)
        [1,3]
        '''
        # Dado que el array está ordenado, puedo realizar una sumatoria de los extremos
        # e ir avanzando hacia el interior        
        for left in range(len(numbers)-1):
            right = len(numbers)-1
            while left < right:
                summ = numbers[left] + numbers[right]
                if summ > target:
                    right -= 1                    
                elif summ < target:                    
                    left += 1
                else:
                    return [left+1, right+1]

class SolutionA:
    '''Solución mediante diccionario (hash) de valores ya vistos'''
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        '''
        Dada una lista de números ordenados (asdending) y un target, devuelve
        un array con los índices (1-index) de los 2 números que suman dicho objetivo.

        >>> twoSum([2,3,4], 6)
        [1,3]
        '''
        seen = {}
        for i, num in enumerate(numbers):
            remaining = target - num

            if remaining in seen:
                return [seen[remaining]+1, i+1]
            else:
                seen[num] = i