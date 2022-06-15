####### LeetCode Problem N° 27: Remove element (Easy) ################
# Given an integer array nums and an integer val,remove all occurrences 
# of val in nums in-place. The relative order of the elements may be changed.
#
# Since it is impossible to change the length of the array in some languages, 
# you must instead have the result be placed in the first part of the array nums. 
# More formally, if there are k elements after removing the duplicates, then 
# the first k elements of nums should hold the final result. 
#
# It does not matter what you leave beyond the first k elements.
# Return k after placing the final result in the first k slots of nums.
# Do not allocate extra space for another array. You must do this by 
# modifying the input array in-place with O(1) extra memory.
#
#
# Example 1:
# Input: nums = [3,2,2,3], val = 3
# Output: 2, nums = [2,2,_,_]
# Explanation: Your function should return k = 2, with the first two elements of nums being 2.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Example 2:
# Input: nums = [0,1,2,2,3,0,4,2], val = 2
# Output: 5, nums = [0,1,4,0,3,_,_,_]
# Explanation: Your function should return k = 5, with the first five elements of nums containing 0, 0, 1, 3, and 4.
# Note that the five elements can be returned in any order.
# It does not matter what you leave beyond the returned k (hence they are underscores).
#
# Constraints:
# 0 <= nums.length <= 100
# 0 <= nums[i] <= 50
# 0 <= val <= 100

class Solution:
    def removeElement(self, nums: list[int], val: int) -> int:
        i = 0
        for num in nums:
            if num != val:
                nums[i] = num
                i += 1
        return i

# Pruebas
test1 = {
    'nums-in': [3,2,2,3],
    'nums': [3,2,2,3],
    'val': 3,
    'output_exp': 2
}
test2 = {
    'nums-in': [0,1,2,2,3,0,4,2],
    'nums': [0,1,2,2,3,0,4,2],
    'val': 2,
    'output_exp': 5
}
tests = [test2]
for test in tests:
    res = Solution().removeElement(test['nums'], test['val'])
    print('Input_Nums: {}\tInput_Val: {}\tResultado esperado: {}\tResultado: {}    Nums_post: {}'\
        .format(test['nums-in'], test['val'], test['output_exp'], res, test['nums']))