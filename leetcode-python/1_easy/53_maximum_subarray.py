######### LeetCode Problem N°53 - Maximum subarray (Easy) ################
# Given an integer array nums, find the contiguous subarray 
# (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
#
# Example 1:
# Input: nums = [-2,1,-3,4,-1,2,1,-5,4]
# Output: 6
# Explanation: [4,-1,2,1] has the largest sum = 6.
#
# Example 2:
# Input: nums = [1]
# Output: 1
#
# Example 3:
# Input: nums = [5,4,-1,7,8]
# Output: 23
#
# Constraints:
# 1 <= nums.length <= 105
# -104 <= nums[i] <= 104
#
# Follow up: If you have figured out the O(n) solution, try coding
#  another solution using the divide and conquer approach, which is more subtle.

class Solution_DP:
    '''Solución utilizando Dynamic Programming'''
    def maxSubArray(self, nums:list[int]) ->int:
        # dp guarda las max_sum posibles hasta la posicion nums[i] (incluyendo ese num)
        # equiv al current_sum de la solución_2 (!= max_sum)
        dp = []

        # valores iniciales
        dp.append(nums[0])
        max_sub = dp[0]

        for i in range(1, len(nums)):
            dp.append(max(dp[i-1] + nums[i], nums[i]))
            max_sub = max(max_sub, dp[i])
            print(f'i: {i}, nums[i]: {nums[i]}, dp[i-1]: {dp[i-1]}, dp[i]: {dp[i]}, max_sub: {max_sub} ')

        return max_sub

class Solution_Simple:
    '''Variante sin necesidad de guardar en memoria la tabla dp'''
    def maxSubArray(self, nums:list[int]) ->int:
        current_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            current_sum = max(current_sum + num, num)
            max_sum = max(max_sum, current_sum)
            print(f'num: {num}, current_sum: {current_sum}, max_sum: {max_sum}')  

        return max_sum    

# Pruebas
test1 = {'nums': [5,4,-1,7,8], 'output_exp': 23}
test2 = {'nums': [-3,-2,-1], 'output_exp': -1}
test3 = {'nums': [-2,1,-3,4,-1,2,1,-5,4], 'output_exp': 6}
test4 = {'nums': [1], 'output_exp': 1}
tests = [test3]
for test in tests:
    res = Solution_DP().maxSubArray(test['nums'])
    print('Input: {}\tResultado esperado: {}\tResultado: {}'\
        .format(test['nums'], test['output_exp'], res))     