############# LeetCode Problem N° 70: Climbing Stairs (Easy) #################
# You are climbing a staircase. It takes n steps to reach the top.
# Each time you can either climb 1 or 2 steps. 
# In how many distinct ways can you climb to the top?
#
# Example 1:
# Input: n = 2
# Output: 2
# Explanation: There are two ways to climb to the top.
# 1. 1 step + 1 step
# 2. 2 steps
#
# Example 2:
# Input: n = 3
# Output: 3
# Explanation: There are three ways to climb to the top.
# 1. 1 step + 1 step + 1 step
# 2. 1 step + 2 steps
# 3. 2 steps + 1 step
#
# Constraints:
# 1 <= n <= 45

class SolutionRecursive:
    '''
    Solución aplicando recursividad.
    La solución para n escalones es la suma de las soluciones parciales
    según decida subir 1 o 2 peldaños en el siguiente paso.
    '''
    # Voy memorizando las variantes para las diferentes cantidades de peldaños
    # las variantes para n son: 1 + variantes(n-1)
    memo = {}

    def climbStairs(self, n: int) -> int:
        # Caso base (sé cuantas variantes hay para 'n' peldaños)
        self.memo[1] = 1
        self.memo[2] = 2

        if n in self.memo: 
            return self.memo[n]

        self.memo[n] = self.climbStairs(n-1) + self.climbStairs(n-2)
        return self.memo[n]

class SolutionDP:
    '''
    Solución aplicando Dynamic Programming. Se guarda una tabla que va
    registrando las variantes para cada cantidad de n peldaños
    '''
    def climbStairs(self, n: int) -> int:
        # Casos conocidos 
        # n: 1 peldaño -> 1 variante -> 1
        # n: 2 peldaños -> 2 variantes -> 1+1 / 2
        if n <= 2: 
            return n

        # inicialiazo dp que guardara las posibilidades para cada 'n'
        dp = [0]*(n+1)

        # cargo los conocidos, base
        dp[0] = 0
        dp[1] = 1
        dp[2] = 2 
        
        # construyo la tabla desde abajo hasta 'n'
        for nn in range(3, n+1):
            dp[nn] = dp[nn-1] + dp[nn-2]
        
        return dp[n]

# Pruebas
test1={'n':2, 'out_exp':2}
test2={'n':3, 'out_exp':3}
test3={'n':4, 'out_exp':5}
test4={'n':5, 'out_exp':8}
test5={'n':6, 'out_exp':13}
tests = [test1, test2, test3, test4, test5]
for test in tests:
    res=SolutionDP().climbStairs(test['n'])
    print('n: {}, resultado: {}, resultado esperado: {}'.format(test['n'], res, test['out_exp']))