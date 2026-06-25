class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # Optimal Solution
        min_price = float('inf')
        max_profit = 0

        for price in prices:
            min_price = min(min_price, price)
            profit = price - min_price
            max_profit = max(profit, max_profit)
        #print(max_profit)
        return max_profit






        # Brute Force
        # Time Complexity: O(n^2)
        # best_day = 0
        # for i in range(len(prices)):
        #     for j in range(i+1, len(prices)):
        #         profit = prices[j] - prices [i]
        #         best_day = max(best_day,profit)
        # # print(best_day)
        # return best_day
