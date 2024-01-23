class Solution:
    def maxProfit_bruitForce(self, prices):
        max_profit = 0
        for i in range(len(prices) -2):
            for j in range(i, len(prices)):
                max_profit = max(max_profit, prices[j]- prices[i])
        return max_profit

    def maxProfit_2pointer(self, prices): # with this solution I was getting time limit exceed
        start = 0
        end = len(prices) -1
        max_profit = 0
        while start < end:
            max_profit = max((prices[end]- prices[start]), max_profit)
            if prices[start] > prices[end]:
                start +=1
            elif prices[end] > prices[start]:
                end -= 1
        return max_profit

    
    def maxProfit_slidingWindow(self, prices): 
        lowest_price = prices[0]
        max_profit = 0
        for price in prices:
            if lowest_price > price:
                lowest_price = price
            max_profit = max(max_profit, price - lowest_price)
        return max_profit
