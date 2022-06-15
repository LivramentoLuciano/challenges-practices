######### LeetCode Problem N°75 - Sort Colors (Medium) ################
# Given an array nums with n objects colored red, white, or blue, 
# sort them in-place so that objects of the same color are adjacent,
# with the colors in the order red, white, and blue.
# We will use the integers 0, 1, and 2 to represent the
# color red, white, and blue, respectively.
#
# You must solve this problem without using the library's sort function.
#
# Example 1:
# Input: nums = [2,0,2,1,1,0]
# Output: [0,0,1,1,2,2]
#
# Example 2:
# Input: nums = [2,0,1]
# Output: [0,1,2]
#
# Constraints:
# n == nums.length
# 1 <= n <= 300
# nums[i] is either 0, 1, or 2.

# Es un dutch flag problem: solución por contador, solución por one-pass

class SolutionCount:
    ''' Resolución de DutchFlag mediante Contadores de cada Color (Valor) '''
    def sortColors(self, nums:list[int]) -> None:
        # Cuento los elementos de cada color
        zeros, ones, twos = 0, 0, 0        
        for num in nums:
            if num == 0: zeros += 1
            elif num == 1: ones += 1
            else: twos += 1
        
        # sobreescribo nums con cada color segun contadores
        nums[0:zeros] = [0]*zeros
        nums[zeros:zeros+ones] = [1]*ones
        nums[zeros+ones:] = [2]*twos

        return None

class SolutionTwoPass:
    def sortColors(self, nums:list[int]) -> None:
        ''' Solución por método Two Pass '''
        # Primero ordeno a la izquierda los 0
        i = 0
        for j in range(len(nums)):
            if nums[j] == 0:
                nums[i], nums[j] = nums[j], nums[i]
                i += 1

        # Ahora ordeno los 1 a continuación
        k = i
        for m in range(i, len(nums)):
            if nums[m] == 1:
                nums[k], nums[m] = nums[m], nums[k]
                k += 1

        return None

class SolutionOnePass:
    def sortColors(self, nums:list[int]) -> None:
        # indices donde colocar los 0's y 2's, y recorrer la lista
        start, end, i = 0, len(nums)-1, 0

        while i <= end:
            if nums[i] == 0:
                # si encuentro un 0 lo swapeo al inicio
                nums[i], nums[start] = nums[start], nums[i]
                start += 1
                i += 1
            elif nums[i] == 2:
                # si encuentro un 2 lo swapeo al final
                nums[i], nums[end] = nums[end], nums[i]
                end -= 1
            else:
                # si encuentro un 1, sigo recorriendo
                i += 1
        return None

test1={'nums_orig': [2,0,2,1,1,0], 'nums':[2,0,2,1,1,0], 'out_exp': [0,0,1,1,2,2]}
tests = [test1]

for test in tests:
    SolutionOnePass().sortColors(test['nums'])
    print('Nums_orig:', test['nums_orig'], 'Resultado esperado:', test['out_exp'], 'Resultado:', test['nums'])
