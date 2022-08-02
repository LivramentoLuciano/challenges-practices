######### LeetCode Problem N°268 - Missing Number (Easy) ################
# Given an array nums containing n distinct numbers in the range [0, n], 
# return the only number in the range that is missing from the array.
#
# Example 1:
# Input: nums = [3,0,1]
# Output: 2
# Explanation: n = 3 since there are 3 numbers, so all numbers are in the range [0,3]. 2 is the missing number in the range since it does not appear in nums.
#
# Example 2:
# Input: nums = [0,1]
# Output: 2
# Explanation: n = 2 since there are 2 numbers, so all numbers are in the range [0,2]. 2 is the missing number in the range since it does not appear in nums.
#
# Example 3:
# Input: nums = [9,6,4,2,3,5,7,0,1]
# Output: 8
# Explanation: n = 9 since there are 9 numbers, so all numbers are in the range [0,9]. 8 is the missing number in the range since it does not appear in nums.
#
# Constraints:
# n == nums.length
# 1 <= n <= 104
# 0 <= nums[i] <= n
# All the numbers of nums are unique.

# Solución más rápida O(n)
class Solution:
    def missingNumber(self, nums: list[int]) -> int:   
        ''' 
        Dada una lista de n números (uniques), devolver el número faltante
        del rango [0,n] (n incluido)
        >>> missingNumer([0,1])
        2
        '''    
        # cargo con -1 todo el rango...     
        res = [-1]*(len(nums)+1)

        # ... coloco el valor x en la posición x
        # y el que falte completar será el faltante
        for x in nums: 
            res[x] = x
        for x in range(len(res)):
            if res[x] == -1:
                return x

class SolutionLower:    
    def missingNumber(self, nums: list[int]) -> int:
        ''' 
        Dada una lista de n números (uniques), devolver el número faltante
        del rango [0,n] (n incluido)
        >>> missingNumer([0,1])
        2
        '''
        nums.sort()
        n = len(nums)
        
        # busco el num faltante contra [0,n)
        for i in range(n):
            if nums[i] != i:
                return i
