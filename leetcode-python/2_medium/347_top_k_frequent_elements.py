######### LeetCode Problem N°347 - Top K Frequent Elements (Medium) ################
# Given an integer array nums and an integer k, return the 
# k most frequent elements. You may return the answer in any order.
#
# Example 1:
# Input: nums = [1,1,1,2,2,3], k = 2
# Output: [1,2]
#
# Example 2:
# Input: nums = [1], k = 1
# Output: [1]
#
# Constraints:
# 1 <= nums.length <= 10**5
# k is in the range [1, the number of unique elements in the array].
# It is guaranteed that the answer is unique.
#
# Follow up: Your algorithm's time complexity must be better than O(n log n), where n is the array's size.

class Solution:
    '''
    Variante Counter + Nuevo Recorrido Counter, obteniendo lista de números
    por frecuencia, en lugar de Sort+Slice, para los Top K.
    Time: O(N)
    '''
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # Contador de Ocurrencias de cada numero
        counter = Counter(nums)

        # Diccionario con Frecuencias y Registro el maximo (ahorra tiempo luego)
        frq, max_count = {}, 0
        for num, cnt in counter.items():
            frq[cnt] = frq.get(cnt, []) + [num]
            max_count = max(max_count, cnt)
        
        # finalmente, genero el resultado, lista ordenada por frecuencia
        most_frequent = []
        for cnt in range(max_count, 0, -1):
            most_frequent.extend(frq.get(cnt, []))
            # Si ya tengo más de K elementos, salgo, no continuo
            if len(most_frequent) >= k:
                return most_frequent[:k]
        
        return most_frequent


from collections import Counter
class SolutionSorted:
    '''
    Solución Counter de ocurrencias + Sort + Slice
    Time: O(N*log(N))
    '''
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        # contabilizo ocurrencias de cada numero y ordeno descending
        counter = Counter(nums)
        most_frequents = sorted(counter, key=counter.get, reverse=True)

        # devuelvo las top K
        return most_frequents[:k]


import heapq
class SolutionHeap:
    '''
    Solución utilizando Heapq en lugar de sort + slice. 
    Time: O(K*log(N))
    '''
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        counter = Counter(nums)
        return heapq.nlargest(k, counter, key=counter.get)


# Pruebas
test1 = {'nums': [1,1,1,2,2,3], 'k': 2, 'output_exp': [1,2]}
test2 = {'nums': [1], 'k': 1, 'output_exp': [1]}
test3 = {'nums': [-1,-1], 'k': 1, 'output_exp': [-1]}
tests = [test1, test2]
tests = [test3]
for test in tests:
    res = Solution().topKFrequent(test['nums'], test['k'])
    print('nums: {}, k: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['k'], test['output_exp'], res))
