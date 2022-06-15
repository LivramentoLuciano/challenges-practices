############ LeetCode Problem N° 9: Palindrome Number (Easy) #################
# Given an integer x, return true if x is palindrome integer.
# An integer is a palindrome when it reads the same backward as forward.
# For example, 121 is a palindrome while 123 is not.
# 
# Ejemplo 1:
# Input: x = 121
# Output: true
#
# Ejemplo 2:
# Input: x = -121
# Output: false
#
# Constraints:
# -2**31 <= x <= 2**31 - 1


class Solution:
    def isPalindrome(self, x: int) -> bool:
        '''
        Devuelve si un numero es palindromo (se puede leer de igual manera en ambos sentidos).
        Basándose en el uso de str(some_int).
        '''
        # numeros negativos NO son palindromos
        if x < 0: return False

        # Convierto el input a string, y luego a lista
        # para poder compararlo con el mismo dado vuelta
        x_str = str(x)
        x_list = list(x_str)

        x_reverse = list(x_list)
        x_reverse.reverse()

        return x_list == x_reverse


    def isPalindrome3(self, x: int) -> bool:
        '''
        Devuelve si un numero es palindromo (se puede leer de igual manera en ambos sentidos).
        Basándose en la division sucesiva del numero para obtener sus diferentes digitos, de 
        esta manera, se puede ir formando el numero 'reverse' y finalmente comparar si son iguales
        '''            
        aux = x
        rev = 0

        # Genero el numero reverseado, a partir de cada digito del original
        while aux > 0:
            dig = aux%10
            rev = rev*10 + dig
            aux = aux//10

        return x == rev


# Performance isPalindrome (usando str()):
# Runtime: 90 ms, faster than 45.21% 
# Memory Usage: 13.8 MB, less than 96.74%
#
# Performance isPalindrome2 (while-reverse)
# Runtime: 82 ms, faster than 56.00%
# Memory Usage: 13.9 MB, less than 60.06%