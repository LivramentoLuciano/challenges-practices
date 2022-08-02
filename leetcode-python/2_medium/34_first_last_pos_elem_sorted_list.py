######## LeetCode Problem N° 34: Find First and Last Position of element in Sorted Array (Medium) ##########
# Given an array of integers nums sorted in non-decreasing order, 
# find the starting and ending position of a given target value.
# If target is not found in the array, return [-1, -1].
# You must write an algorithm with O(log n) runtime complexity.
#
# Example 1:
# Input: nums = [5,7,7,8,8,10], target = 8
# Output: [3,4]
#
# Example 2:
# Input: nums = [5,7,7,8,8,10], target = 6
# Output: [-1,-1]
#
# Example 3:
# Input: nums = [], target = 0
# Output: [-1,-1]
#
# Constraints:
# - 0 <= nums.length <= 10**5
# - -10**9 <= nums[i] <= 10**9
# - nums is a non-decreasing array.
# - -10**9 <= target <= 10**9

class Solution:
    def searchRange(self, nums: list[int], target: int) -> list[int]:
        '''
        Dada una lista ordenada ascendentemente "nums", devuelve la primera
        y última aparición del "target". Emplea para su búsqueda Binary Search.
        '''
        # Algoritmo
        # Se implementan 2 funciones de búsqueda binaria:
        #   - Búsqueda del primer índice de aparición de "target"
        #   - Búsqueda del último índice de aparición de "target"
        res = [-1, -1]
        res[0] = self.search_first_index(nums, target)
        res[1] = self.search_last_index(nums, target)     
        return res

    # Funciones de Búsqueda First/Last (Binary Search)
    # Son Binary Search modificados para no detenerse ante la primera aparición
    # del target, sino que continuarán buscando hasta encontrar el FIRST (Más a la izquierda)
    # o el LAST (Más a la derecha)
    def search_last_index(self, nums:list[int], target:int) -> int:
        '''
        Devuelve la posición de la última aparición del "target" 
        dentro de "nums". Implementando Binary Search.
        
        >>> search_last_index([5,7,7,8,8,10], 8)
        4
        '''
        # último index (más a la derecha)
        index = -1

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                # encontró target, actualizo index (NO SALGO)
                # sigo buscando hacia la derecha
                index = mid
                lo = mid + 1

        return index

    def search_first_index(self, nums:list[int], target:int) -> int:
        '''
        Devuelve la posición de la primera aparición del "target" 
        dentro de "nums". Implementando Binary Search.
        
        >>> search_first_index([5,7,7,8,8,10], 8)
        3
        '''
        # Primer index (más a la izquierda)
        index = -1

        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo + hi) // 2
            
            if nums[mid] < target:
                lo = mid + 1
            elif nums[mid] > target:
                hi = mid - 1
            else:
                # encontró target, actualizo index (NO SALGO)
                # sigo buscando hacia la izquierda
                index = mid
                hi = mid - 1

        return index


# Pruebas
test1 = {'nums': [5,7,7,8,8,10], 'target': 8, 'output_exp': [3,4]}
test2 = {'nums': [5,7,7,8,8,10], 'target': 6, 'output_exp': [-1,-1]}
test3 = {'nums': [], 'target': 0, 'output_exp': [-1,-1]}
tests = [test1, test2, test3]
for test in tests:
    res = Solution().searchRange(test['nums'], test['target'])
    print('nums: {}, target: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['target'], test['output_exp'], res))
