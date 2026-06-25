class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        best_day = 0
        for i in range(len(prices)):
            for j in range(i+1, len(prices)):
                profit = prices[j] - prices [i]
                best_day = max(best_day,profit)
        # print(best_day)
        return best_day
