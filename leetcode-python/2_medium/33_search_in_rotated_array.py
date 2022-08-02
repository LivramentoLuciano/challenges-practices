############ LeetCode Problem N° 33: Search in Rotated Sorted Array (Medium) #################
# There is an integer array nums sorted in ascending order (with distinct values).
# Prior to being passed to your function, nums is possibly rotated at an unknown pivot
# index k (1 <= k < nums.length) such that the resulting array is 
# [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). 
# For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].
#
# Given the array nums after the possible rotation and an integer target, return the index of 
# target if it is in nums, or -1 if it is not in nums. You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [4,5,6,7,0,1,2], target = 0
# Output: 4
#
# Example 2:
# Input: nums = [4,5,6,7,0,1,2], target = 3
# Output: -1
#
# Example 3:
# Input: nums = [1], target = 0
# Output: -1
#
# Constraints:
# - 1 <= nums.length <= 5000
# - -10**4 <= nums[i] <= 10**4
# - All values of nums are unique.
# - nums is an ascending array that is possibly rotated.
# - -10**4 <= target <= 10**4

class Solution:
    def search(self, nums: list[int], target: int) -> int:
        '''
        Dada una lista...
        Utiliza Binary Search.
        '''
        left, right = 0, len(nums)
        while (left < right):
            mid = (right + left) // 2

            # num: numero del centro (se aplica +/- inf sobre el intervalo rotado
            # que no me sirve, para poder implementar binary search normal en el restante)
            if (nums[mid] < nums[0]) == (target < nums[0]):
                # - [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], target: 5, mid=6
                # - [12, 13, 14, 15, 16, 17, 18, 19, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11], target: 13, mid=16
                num = nums[mid]
            else:
                # - [-inf, -inf, -inf, -inf, -inf, -inf, -inf, -inf, 0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11]
                # - [12, 13, 14, 15, 16, 17, 18, 19, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf, inf]
                num = float('-inf') if target < nums[0] else float('inf')

            # Una vez colocado +-inf, puedo hacer binary search normal
            if num > target:
                right = mid
            elif num < target:
                left = mid + 1
            else:
                return mid                  

        return -1


# Pruebas
test1 = {'nums': [4,5,6,7,0,1,2], 'target': 0, 'output_exp': 4}
test2 = {'nums': [], 'target': 3, 'output_exp': -1}
test3 = {'nums': [1], 'target': 0, 'output_exp': -1}
test4 = {'nums': [4,5,6,7,0,1,2], 'target': 3, 'output_exp': -1}
test5 = {'nums': [1], 'target': 1, 'output_exp': 0}
test6 = {'nums': [1,3], 'target': 1, 'output_exp': 0}
tests = [test1, test2, test3, test4]
for test in tests:
    res = Solution().search(test['nums'], test['target'])
    print('nums: {}, target: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['target'], test['output_exp'], res))

