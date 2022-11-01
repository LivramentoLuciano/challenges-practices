########## LeetCode Problem N°39 - Combination Sum (Medium) ################
# Given an array of distinct integers candidates and a target integer target, 
# return a list of all unique combinations of candidates where the 
# chosen numbers sum to target. You may return the combinations in any order.
#
# The same number may be chosen from candidates an unlimited number of times. 
# Two combinations are unique if the frequency of at least one of the chosen numbers is different.
# The test cases are generated such that the number of unique combinations 
# that sum up to target is less than 150 combinations for the given input.
#
# Example 1:
# Input: candidates = [2,3,6,7], target = 7
# Output: [[2,2,3],[7]]
# Explanation:
# 2 and 3 are candidates, and 2 + 2 + 3 = 7. Note that 2 can be used multiple times.
# 7 is a candidate, and 7 = 7.
# These are the only two combinations.
#
# Example 2:
# Input: candidates = [2,3,5], target = 8
# Output: [[2,2,2,2],[2,3,3],[3,5]]
#
# Example 3:
# Input: candidates = [2], target = 1
# Output: []
#
# Constraints:
# - 1 <= candidates.length <= 30
# - 2 <= candidates[i] <= 40
# - All elements of candidates are distinct.
# - 1 <= target <= 40
class SolutionTraverse:
    def combinationSum(self, candidates: list[int], target: int) -> list[list[int]]:
        '''
        Dada una lista de números (sin repetir), y un número objetivo, 
        devuelve todas las combinaciones posibles (únicas), que utilizando
        cualquier cantidad de veces cada número, suman el "target" deseado.

        >>> combinationSum([2,3,6,7], 7)
        [[2,2,3],[7]]
        '''
        self.res = []
        def traverse(cands, currComb, currSum):
            if currSum == target: self.res.append(currComb)
            if currSum >= target: return
            for i in range(len(cands)):
                traverse(cands[i:], currComb + [cands[i]], currSum + cands[i])    
        traverse(candidates, [], 0)
        return self.res


# Pruebas
test1 = {'candidates': [2,3,6,7], 'target': 7, 'output_exp': [[2,2,3],[7]]}
test2 = {'candidates': [2,3,5], 'target': 8, 'output_exp': [[2,2,2,2],[2,3,3],[3,5]]}
test3 = {'candidates': [2], 'target': 1, 'output_exp': []}
tests = [test1]
for test in tests:
    res = SolutionTraverse().combinationSum(test['candidates'], test['target'])
    print('candidates: {} target: {} - Resultado esperado: {} - Resultado: {}'\
        .format(test['candidates'], test['target'], test['output_exp'], res))

        