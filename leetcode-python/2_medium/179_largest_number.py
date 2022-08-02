########## LeetCode Problem N°179 - Largest Number (Medium) ################
# Given a list of non-negative integers nums, arrange them 
# such that they form the largest number and return it.
# Since the result may be very large, so you need to return a string instead of an integer.
#
# Example 1:
# Input: nums = [10,2]
# Output: "210"
#
# Example 2:
# Input: nums = [3,30,34,5,9]
# Output: "9534330"
#
# Constraints:
# 1 <= nums.length <= 100
# 0 <= nums[i] <= 109

from functools import cmp_to_key
class Solution:
    def largestNumber(self, nums: list[int]) -> str:
        def nums_compare(a,b):
            '''Comparador customizado'''
            # si el numero ab es mayor a ba
            return int(a+b) - int(b+a)

        if not nums: return ''
        if sum(nums) == 0: return '0'

        strnums_sorted = sorted(map(str,nums), key=cmp_to_key(nums_compare), reverse=True)
        largest = ''.join(strnums_sorted)
        return largest

# Pruebas
test1 = {'nums': [10,2], 'output_exp': '210'}
test2 = {'nums': [3,30,34,5,9], 'output_exp': '9534330'}
test3 = {'nums': [35,351], 'output_exp': '9534330'}
test4 = {'nums': [35,355], 'output_exp': '9534330'}
test5 = {'nums': [0,0], 'output_exp': '0'}
tests = [test2]
for test in tests:
    res = Solution().largestNumber(test['nums'])
    print('Nums: {}\tResultado esperado: {}\tResultado: {}'.format(test['nums'], test['output_exp'], res))    
