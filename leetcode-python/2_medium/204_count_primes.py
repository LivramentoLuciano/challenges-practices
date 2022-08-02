######### LeetCode Problem N°204 - Count Primes (Medium) ################
# Given an integer n, return the number of prime numbers that are strictly less than n.
#
# Example 1:
# Input: n = 10
# Output: 4
# Explanation: There are 4 prime numbers less than 10, they are 2, 3, 5, 7.
#
# Example 2:
# Input: n = 0
# Output: 0
#
# Example 3:
# Input: n = 1
# Output: 0
#
# Constraints:
# 0 <= n <= 5*10**6

class Solution:
    def countPrimes(self, n: int) -> int:
        # casos base
        if n <= 2: return 0

        # La forma correcta, será realizarlo por medio de la Criba de Eratóstenes
        # que nos permite hallar todos los números primos dentro de un determinado rango
        # a partir de los múltiplos, sin necesidad de iterar y buscar divisores de cada numero
        primes =  [True for i in range(n)]
        primes[0], primes[1] = False, False

        # marco con False todos los distintos múltiplos de los números
        # hasta el número tal que X**2 sea mayor que el n límite (rango)
        # los que queden sin marcar serán Primos
        last = int(n**0.5)+1
        for i in range(2, last+1):
            if primes[i] == False: continue
            # multiplos de i, comenzando en i*i, evita repetir ya visitados
            for m in range(i*i, n, i):
                primes[m] = False

        return sum(primes)

# Pruebas
test1={'n': 10, 'out_exp': 4}
test2={'n': 0, 'out_exp': 0}
test3={'n': 1, 'out_exp': 0}
test4={'n': 100, 'out_exp': 25}
test5={'n': 5000000, 'out_exp': 348513}
tests = [test1,test2, test3]
tests = [test5]
for test in tests:
    res = Solution().countPrimes(test['n'])
    print('n: {} - Resultado esperado: {} - Resultado: {}'.format(test['n'], test['out_exp'], res))