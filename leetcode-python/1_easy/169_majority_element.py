############ LeetCode Problem N° 169: Majority Element (Easy) #################
# Given an array nums of size n, return the majority element.
# The majority element is the element that appears more than ⌊n / 2⌋ times. 
# You may assume that the majority element always exists in the array.
#
# Example 1:
# Input: nums = [3,2,3]
# Output: 3
#
# Example 2:
# Input: nums = [2,2,1,1,1,2,2]
# Output: 2
#
# Constraints:
# n == nums.length
# 1 <= n <= 5 * 104
# -109 <= nums[i] <= 109

class Solution:
    '''Solución One Pass. Time: O(N), Space: O(1)'''
    def majorityElement(self, nums: list[int]) -> int:
        candidate, count = None, 0
        for num in nums:
            if count == 0:
                candidate = num
            count = count + 1 if num == candidate else count - 1
        
        return candidate
            
from collections import Counter
class SolutionA:
    '''Solución básica mediante Contador de ocurrencias. Two-Pass. Space: O(N)'''
    def majorityElement(self, nums: list[int]) -> int:
        n = len(nums)
        counter = Counter(nums)
        for num, count in counter.items():
            if count > n/2:
                return num


# Pruebas
test1 = {'nums': [3,2,3], 'output_exp': 3}
test2 = {'nums': [2,2,1,1,1,2,2], 'output_exp': 2}
tests = [test1, test2]
for test in tests:
    res = Solution().majorityElement(test['nums'])
    print('nums: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['output_exp'], res))        