######### LeetCode Problem N°412 - Fizz Buzz (Easy) ################
# Given an integer n, return a string array answer (1-indexed) where:
# - answer[i] == "FizzBuzz" if i is divisible by 3 and 5.
# - answer[i] == "Fizz" if i is divisible by 3.
# - answer[i] == "Buzz" if i is divisible by 5.
# - answer[i] == i (as a string) if none of the above conditions are true.
#
# Example 1:
# Input: n = 3
# Output: ["1","2","Fizz"]
#
# Example 2:
# Input: n = 5
# Output: ["1","2","Fizz","4","Buzz"]
#
# Example 3:
# Input: n = 15
# Output: ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]
#
# Constraints:
# 1 <= n <= 104

class Solution:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = []
        for i in range(1, n+1):
            ans = ""
            if not (i % 3 == 0 or i % 5 == 0): ans = str(i)
            if i % 3 == 0: ans = "Fizz"
            if i % 5 == 0: ans += "Buzz"
            answer.append(ans)
        return answer

class SolutionListCompr:
    def fizzBuzz(self, n: int) -> list[str]:
        answer = [
            'FizzBuzz' 
            if i % 15 == 0 else 'Buzz' 
            if i % 5 == 0 else 'Fizz'
            if i % 3 == 0 else str(i)            
            for i in range(1, n+1)
        ]
        return answer


# Pruebas
test1 = {'n': 3, 'output_exp': ["1","2","Fizz"]}
test2 = {'n': 4, 'output_exp': ["1","2","Fizz","4"]}
test2 = {'n': 15, 'output_exp': ["1","2","Fizz","4","Buzz","Fizz","7","8","Fizz","Buzz","11","Fizz","13","14","FizzBuzz"]}
tests = [test2]
for test in tests:
    res = SolutionListCompr().fizzBuzz(test['n'])
    print('s: {} - Resultado esperado: {} - Resultado: {}'\
        .format(test['n'], test['output_exp'], res))    