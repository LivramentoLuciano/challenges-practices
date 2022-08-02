######### LeetCode Problem N°454 - 4 Sum II (Medium) ################
# Given four integer arrays nums1, nums2, nums3, and nums4 all 
# of length n, return the number of tuples (i, j, k, l) such that:
#   - 0 <= i, j, k, l < n
#   - nums1[i] + nums2[j] + nums3[k] + nums4[l] == 0
#
# Example 1:
# Input: nums1 = [1,2], nums2 = [-2,-1], nums3 = [-1,2], nums4 = [0,2]
# Output: 2
# Explanation:
# The two tuples are:
# 1. (0, 0, 0, 1) -> nums1[0] + nums2[0] + nums3[0] + nums4[1] = 1 + (-2) + (-1) + 2 = 0
# 2. (1, 1, 0, 0) -> nums1[1] + nums2[1] + nums3[0] + nums4[0] = 2 + (-1) + (-1) + 0 = 0
#
# Example 2:
# Input: nums1 = [0], nums2 = [0], nums3 = [0], nums4 = [0]
# Output: 1
#
# Constraints:
#   - n == nums1.length
#   - n == nums2.length
#   - n == nums3.length
#   - n == nums4.length
#   - 1 <= n <= 200
#   - -2**28 <= nums1[i], nums2[i], nums3[i], nums4[i] <= 2**28

class Solution:
    def fourSumCount(self, nums1: list[int], nums2: list[int], nums3: list[int], nums4: list[int]) -> int:
        # Algoritmo:
        # Guardo en un diccionario todas las sumas posibles de las listas nums1, nums2
        # Luego, recorro nums3, nums4, y acumulo todas las veces que encuentre una suma = -(X)
        # siendo X, cada una de las sumatorias de 1 y 2
        sums, res = {}, 0

        # Todas las sumatorias posibles de nums1 y nums2
        for n1 in nums1:
            for n2 in nums2:
                sums[n1+n2] = sums.get(n1+n2, 0) + 1
        
        # Recorro nums3 y nums4, buscando el opuesto, que dará una suma total=0
        for n3 in nums3:
            for n4 in nums4:
                res += sums.get(-(n3+n4), 0)
        
        # return sum(sums.get(-(n3+n4),0) for n3 in nums3 for n4 in nums4)
        return res


# Pruebas
test1 = {'nums1': [1,2], 'nums2': [-2,-1], 'nums3': [-1,2], 'nums4': [0,2], 'output_exp': 2}
test2 = {'nums1': [0], 'nums2': [0], 'nums3': [0], 'nums4': [0], 'output_exp': 1}
tests = [test1, test2]
for test in tests:
    res = Solution().fourSumCount(test['nums1'], test['nums2'], test['nums3'], test['nums4'])
    print('nums1: {}, nums2: {}, nums3: {}, nums4: {}'.format(test['nums1'][:5], test['nums2'][:5], test['nums3'][:5], test['nums4'][:5]))
    print('Resultado esperado: {} - Resultado: {}'.format(test['output_exp'], res))