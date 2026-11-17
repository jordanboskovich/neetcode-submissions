class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        buy_price = 101
        profit = 0
        for price in prices:
            sell_price = price
            if price < buy_price:
                buy_price = price
            if sell_price - buy_price > profit:
                profit = sell_price - buy_price 
        return profit