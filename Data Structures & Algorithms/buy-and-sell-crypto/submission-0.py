class Solution:
    def maxProfit(self, prices: list[int]) -> int:
        min_price = float('inf')  # set to infinity initially
        max_profit = 0

        for price in prices:
            if price < min_price:
                min_price = price  # found a better day to buy
            else:
                profit = price - min_price  # possible profit
                max_profit = max(max_profit, profit)  # update max profit if it's better

        return max_profit
