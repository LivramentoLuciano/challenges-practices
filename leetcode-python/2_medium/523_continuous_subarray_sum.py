######### LeetCode Problem N°523 - Continuous Subarray Sum (Medium) ################
# Given an integer array nums and an integer k, return true if nums has a continuous
# subarray of size at least two whose elements sum up to a multiple of k, or false otherwise.
# An integer x is a multiple of k if there exists an integer n such that x = n * k. 
# 0 is always a multiple of k.
#
# Example 1:
# Input: nums = [23,2,4,6,7], k = 6
# Output: true
# Explanation: [2, 4] is a continuous subarray of size 2 whose elements sum up to 6.
#
# Example 2:
# Input: nums = [23,2,6,4,7], k = 6
# Output: true
# Explanation: [23, 2, 6, 4, 7] is an continuous subarray of size 5 whose elements sum up to 42.
# 42 is a multiple of 6 because 42 = 7 * 6 and 7 is an integer.
#
# Example 3:
# Input: nums = [23,2,6,4,7], k = 13
# Output: false
#
# Constraints:
# 1 <= nums.length <= 105
# 0 <= nums[i] <= 109
# 0 <= sum(nums[i]) <= 231 - 1
# 1 <= k <= 231 - 1

class Solution:
    def checkSubarraySum(self, nums: list[int], k: int) -> bool:
        seen = {0: -1}
        curr_sum = 0
        
        for i, num in enumerate(nums):
            curr_sum = (curr_sum + num) % k
            print('i:', i, 'current_sum =', curr_sum)
            
            if curr_sum not in seen:
                seen[curr_sum] = i
            elif i - seen[curr_sum] >= 2:
                    return True
        
        return False

# Pruebas
test1 = {'nums': [23,2,4,6,7], 'k': 6, 'output_exp': True}
test2 = {'nums': [23,2,6,4,7], 'k': 6, 'output_exp': True}
test3 = {'nums': [23,2,6,4,7], 'k': 13, 'output_exp': False}
test4 = {'nums': [1,0], 'k': 2, 'output_exp': False}
tests = [test1, test2, test3, test4]
tests = [test1]
for test in tests:
    res = Solution().checkSubarraySum(test['nums'], test['k'])
    print('nums: {}, k: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['k'], test['output_exp'], res))
