######### LeetCode Problem N°287 - Find Duplicate Number (Medium) ################
# Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.
# There is only one repeated number in nums, return this repeated number.
# You must solve the problem without modifying the array nums and uses only constant extra space.
#
# Example 1:
# Input: nums = [1,3,4,2,2]
# Output: 2
#
# Example 2:
# Input: nums = [3,1,3,4,2]
# Output: 3
#
# Constraints:
#   - 1 <= n <= 10**5
#   - nums.length == n + 1
#   - 1 <= nums[i] <= n
#   - All the integers in nums appear only once except for precisely one integer which appears two or more times.
#
# Follow up:
#   - How can we prove that at least one duplicate number must exist in nums?
#   - Can you solve the problem in linear runtime complexity?

class Solution:
    ''''''
    def findDuplicate(self, nums: list[int]) -> int:
        # Algoritmo:
        # En primer lugar, podemos establecer que habrá al menos 1 repetido
        # dado que el Conjunto Base: [1,n] y len(nums)=n+1
        # Luego, la resolución cumpliendo con los requerimientos de complejidad
        # se basaría en buscar la mediana en el conjunto base y contrastar cuántos 
        # números hay superiores e inferiores en el conjunto "nums", asi detectar
        # en qué intervalo se encuentra el repetido. 
        # Se realiza este proceso iterativamente hasta dar con el valor repetido unívocamente
        # mediante una Binary Search
        n = len(nums)-1
        l, r, median = 0, n, (n+1) // 2

        while l + 1 < r:
            if sum(num <= median for num in nums) > median:
                r = median
            else:
                l = median
            median = (l + 1 + r) // 2
        
        return median

class SolutionIni2:
    '''Variante Solución básica, fines demostrativos. No cumple requerimientos de Complexity'''
    def findDuplicate(self, nums: list[int]) -> int:
        # Resuelto con un contador de ocurrencias
        # Space: O(N); Time: O()
        count = {}
        for num in nums:
            count[num] = count.get(num, 0) + 1
        
        for num, cnt in count.items():
            if cnt > 1:
                return num

class SolutionIni:
    '''Solución básica, fines demostrativos. No cumple requerimientos de Complexity'''
    def findDuplicate(self, nums: list[int]) -> int:
        sorted_nums = sorted(nums)
        for i in range(1, len(sorted_nums)):
            if sorted_nums[i] == sorted_nums[i-1]:
                return sorted_nums[i]


# Pruebas
test1 = {'nums': [1,3,4,2,2], 'output_exp': 2}
test2 = {'nums': [3,1,3,4,2], 'output_exp': 3}
test3 = {'nums': [3, 2, 4, 4, 1, 5], 'output_exp': 4}
tests = [test1, test2]
tests = [test3]
for test in tests:
    res = Solution().findDuplicate(test['nums'])
    print('nums: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['output_exp'], res))