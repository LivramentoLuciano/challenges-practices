######### LeetCode Problem N°4 - Median Arrays (Hard) ################
# Given two sorted arrays nums1 and nums2 of size m and n respectively,
# return the median of the two sorted arrays.
# The overall run time complexity should be O(log (m+n)).
#
# Example 1:
# Input: nums1 = [1,3], nums2 = [2]
# Output: 2.00000
# Explanation: merged array = [1,2,3] and median is 2.
#
# Example 2:
# Input: nums1 = [1,2], nums2 = [3,4]
# Output: 2.50000
# Explanation: merged array = [1,2,3,4] and median is (2 + 3) / 2 = 2.5.
#
# Constraints:
# nums1.length == m
# nums2.length == n
# 0 <= m <= 1000
# 0 <= n <= 1000
# 1 <= m + n <= 2000
# -106 <= nums1[i], nums2[i] <= 106

# TODO: Pedia Time complexity = O(log(n+m))
class Solution:
    def findMedianSortedArrays(self, nums1: list[int], nums2: list[int]) -> float:
        # Combino las listas
        nums_merged = list(nums1)
        nums_merged.extend(nums2)
        nums_merged.sort()
        
        nums_len = len(nums_merged)
        
        if nums_len%2 == 0:
            # si nums, n par de elementos: mediana es promedio entre los dos centrales...
            median = (nums_merged[nums_len//2 - 1] + nums_merged[nums_len//2]) / 2        
        else:
            # ... si n impar de numeros: mediana es el numero del centro
            median = float(nums_merged[nums_len//2])
        
        return median

test1 = {
    'nums1': [],
    'nums2': [1],
    'out_exp': 1
}

test2 = {
    'nums1': [1],
    'nums2': [1],
    'out_exp': 1
}

test3 = {
    'nums1': [1,2],
    'nums2': [1000],
    'out_exp': 2
}

test4 = {
    'nums1': [-1],
    'nums2': [1],
    'out_exp': 0
}

test5 = {
    'nums1': [-1, -5, -8],
    'nums2': [-10, -12, -100],
    'out_exp': -9
}

tests = [test1, test2, test3, test4, test5]
for test in tests:
    res = Solution().findMedianSortedArrays(test['nums1'], test['nums2'])
    print('Nums1: {}\tNums2: {}\tResultado Esperado: {}\tResultado: {}'\
        .format(test['nums1'], test['nums2'], test['out_exp'], res))