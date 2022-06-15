# Given n pairs of parentheses, write a function 
# to generate all combinations of well-formed parentheses.
#
# Example 1:
# Input: n = 3
# Output: ["((()))","(()())","(())()","()(())","()()()"]
#
# Example 2:
# Input: n = 1
# Output: ["()"]
#
# Constraints:
# 1 <= n <= 8

# TODO

class Solution:
    def generateParenthesis(self, n: int) -> list[str]:
        def generate(p, left, right, parens=[]):   
            print('p:', p, 'left:',  left, 'right:', right)         
            if left:         generate(p + '(', left-1, right)
            if right > left: generate(p + ')', left, right-1)
            if not right:    
                parens.append(p)
                print(parens)
            return parens
        return generate('', n, n)


# Pruebas
test1 = {'n': 1, 'output_exp': ['()']}
test2 = {'n': 2, 'output_exp': ['()()', '(())']}
test3 = {'n': 3, 'output_exp': ['()()()', '(()())', '(())()', '()(())', '((()))']}
test4 = {'n': 4, 'output_exp': ["(((())))","((()()))","((())())","((()))()","(()(()))", "(()()())","(()())()",\
                                "(())(())","(())()()","()((()))","()(()())","()(())()","()()(())","()()()()"]}

tests = [test2]
for test in tests:
    res = Solution().generateParenthesis(test['n'])
    print('n: {}\tResultado esperado: {}\tResultado: {}'\
        .format(test['n'], test['output_exp'], res))  
