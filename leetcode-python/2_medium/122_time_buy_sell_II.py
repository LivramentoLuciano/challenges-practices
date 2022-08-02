########## LeetCode Problem N°121 - Best Time to Buy/Sell II (Medium) ################
# You are given an integer array prices where prices[i] is the price of a given stock on the ith day.
# On each day, you may decide to buy and/or sell the stock. You can only hold at most 
# one share of the stock at any time. However, you can buy it then immediately sell it on the same day.
# Find and return the maximum profit you can achieve.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 7
# Explanation: Buy on day 2 (price = 1) and sell on day 3 (price = 5), profit = 5-1 = 4.
# Then buy on day 4 (price = 3) and sell on day 5 (price = 6), profit = 6-3 = 3.
# Total profit is 4 + 3 = 7.
#
# Example 2:
# Input: prices = [1,2,3,4,5]
# Output: 4
# Explanation: Buy on day 1 (price = 1) and sell on day 5 (price = 5), profit = 5-1 = 4.
# Total profit is 4.
#
# Example 3:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: There is no way to make a positive profit, so we never buy the stock to achieve the maximum profit of 0.
#
# Constraints:
# - 1 <= prices.length <= 3*10**4
# - 0 <= prices[i] <= 10**4

# Aplicando Dynamic Programming
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         # dp[i] -> maximo profit vendiendo en el día 'i'
#         dp = [0]*len(prices)


class Solution:
    '''Solución más simple, acumulando las ganancias diarias. Space O(1)'''
    def maxProfit(self, prices: list[int]) -> int:
        # Algoritmo
        # Al poder comprar y vender varias veces, simplemente debo
        # acumular los dias de ganancias y listo
        acum_profit = 0
        for i in range(1, len(prices)):
            day_profit = prices[i] - prices[i-1]
            if day_profit > 0:
                acum_profit += day_profit
        
        return acum_profit

class SolutionOneLiner:
    '''variante de la solución por acumulación, resuelto en una sola línea mediante Zip+Sum'''
    def maxProfit(self, prices: list[int]) -> int:
        # Algoritmo:
        # Zip me empareja prices y prices[1:] -> a: día actual, b: día siguiente
        # Sumo ganancias, colocando un 0 cuando un día fuera negativo
        return sum(max(0, b-a) for a,b in zip(prices, prices[1:]))      

# Pruebas
test1 = {'prices': [7,1,5,3,6,4], 'output_exp': 7}
test2 = {'prices': [1,2,3,4,5], 'output_exp': 4}
test3 = {'prices': [7,6,4,3,1], 'output_exp': 0}
tests = [test3]
for test in tests:
    res = Solution().maxProfit(test['prices'])
    print('Precios: {}\tResultado esperado: {}\tResultado: {}'.format(test['prices'], test['output_exp'], res))    
