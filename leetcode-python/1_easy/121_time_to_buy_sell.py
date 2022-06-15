########## LeetCode Problem N°121 - Time to BuySell (Easy) ################
# You are given an array prices where prices[i] 
# is the price of a given stock on the ith day.
# You want to maximize your profit by choosing a single day to buy one 
# stock and choosing a different day in the future to sell that stock.
#
# Return the maximum profit you can achieve from this transaction. 
# If you cannot achieve any profit, return 0.
#
# Example 1:
# Input: prices = [7,1,5,3,6,4]
# Output: 5
# Explanation: Buy on day 2 (price = 1) and sell on day 5 (price = 6), profit = 6-1 = 5.
# Note that buying on day 2 and selling on day 1 is not allowed because you must buy before you sell.
#
# Example 2:
# Input: prices = [7,6,4,3,1]
# Output: 0
# Explanation: In this case, no transactions are done and the max profit = 0.
#
# Constraints:
# 1 <= prices.length <= 105
# 0 <= prices[i] <= 104

## TODO: Result -> Time exceeded, busqueda lineal no sirve
# class Solution:
#     def maxProfit(self, prices: list[int]) -> int:
#         # Mínimo mejor profit = 0
#         # No hay transacción que de ganancias
#         max_profit = 0

#         for buy_day, buy_price in enumerate(prices[:-1]):
#             for sell_day, sell_price in enumerate(prices[buy_day+1:]):
#                 profit = sell_price - buy_price
#                 max_profit = max(max_profit, profit)        
#         return max_profit


class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        # Mínimo mejor profit = 0
        # No hay transacción que de ganancias
        max_profit = 0
        current_profit = 0

        for day,price in enumerate(prices):
            if day > 0:
                # Calculo profit de ayer a hoy..
                day_profit = price - prices[day-1]

                # ... comparo con el acumulado y me quedo con el maximo
                # (descarta acumulados de dias anteriores si eran de perdidas)
                acum_profit = max(acum_profit + day_profit, day_profit)

                # comparo el acumulado hasta este dia contra el ultimo maximo
                max_profit = max(max_profit, acum_profit)

                print(f'price: {price}, day_profit: {day_profit}, current_profit: {current_profit}, max_profit: {max_profit}')  

        return max_profit

# Pruebas
test1 = {'prices': [7,1,5,3,6,4], 'output_exp': 5}
test2 = {'prices': [7,6,4,3,1], 'output_exp': 0}
test3 = {'prices': [10,7,6,2,10, 12], 'output_exp': 10}
tests = [test3]
for test in tests:
    res = Solution().maxProfit(test['prices'])
    print('Precios: {}\tResultado esperado: {}\tResultado: {}'\
        .format(test['prices'], test['output_exp'], res))    