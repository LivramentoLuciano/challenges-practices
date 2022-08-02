############ LeetCode Problem N° 15: 3 Sum (Medium) #################
# Given an integer array nums, return all the triplets [nums[i], nums[j], nums[k]]
# such that i != j, i != k, and j != k, and nums[i] + nums[j] + nums[k] == 0.
# Notice that the solution set must not contain duplicate triplets.
#
# Example 1:
# Input: nums = [-1,0,1,2,-1,-4]
# Output: [[-1,-1,2],[-1,0,1]]
#
# Example 2:
# Input: nums = []
# Output: []
#
# Example 3:
# Input: nums = [0]
# Output: []
#
# Constraints:
# 0 <= nums.length <= 3000
# -105 <= nums[i] <= 105

class Solution:
    def threeSum(self, nums: list[int]) -> list[list[int]]:
        ''' Dado un array de nums, devuelve las ternas que sumen 0 (sin repetir) '''
        # El funcionamiento se va a basar en recorrer con i, j, k el array buscando las ternas
        # Pero se debe implementar un algoritmo que permita restringir la busqueda, para no 
        # tener que recorrerlo por completo
        # Entonces, se realiza lo siguiente:
        #   1- Ordenamos el array de menor a mayor
        #   2- Con el par i,j buscamos el k que nos de 0, empezando en el final
        #       - Si la suma con el k-esimo es == 0, agrego a los resultados y corto esa busqueda para i;j
        #       - Si la suma con el k-esimo es < 0, corto esa busqueda para i;j ya q k menor no servirá
        #       - Si la suma con el k-esimo es > 0, sigo buscando

        # casos edge
        if len(nums) < 3: return []

        nums = sorted(nums)
        res = set()
        for i in range(len(nums)-2):
            # omito busqueda para este nums[i]:
            #   - si es positivo (por ordenada de menor a mayor)
            #   - si ya fueron buscadas ternas con este nums[i]
            if nums[i] > 0: break
            if i > 0 and nums[i] == nums[i-1]: continue

            j, k = i+1, len(nums)-1           
            while j < k:
                summ = nums[i] + nums[j] + nums[k]
                if summ == 0:
                    # encontré la terna (única para cada i;j)
                    res.add((nums[i], nums[j], nums[k]))
                if summ > 0:
                    # sigo buscando con k menor
                    k -= 1
                else:
                    # (si summ < 0, o ya encontre la terna)
                    # no sirve seguir buscando k menor
                    j += 1

        return [list(triplet) for triplet in res]


# Pruebas
test1 = {'nums': [-1,0,1,2,-1,-4], 'output_exp': [[-1,-1,2],[-1,0,1]]}
test2 = {'nums': [], 'output_exp': []}
test3 = {'nums': [0], 'output_exp': []}
test4 = {'nums': [-2,0,1,1,2], 'output_exp': [[-2,0,2],[-2,1,1]]}
test5 = {'nums': [3,0,-2,-1,1,2], 'output_exp': [[-2,-1,3],[-2,0,2],[-1,0,1]]}
test6 = {'nums': [-1,0,1,2,-1,-4,-2,-3,3,0,4], 'output_exp': [[-4,0,4],[-4,1,3],[-3,-1,4],[-3,0,3],[-3,1,2],[-2,-1,3],[-2,0,2],[-1,-1,2],[-1,0,1]]}
tests = [test1, test2, test3, test4, test5, test6]
for test in tests:
    res = Solution().threeSum(test['nums'])
    print('nums: {} - Resultado esperado: {} - Resultado: {}'.format(test['nums'], test['output_exp'], res))