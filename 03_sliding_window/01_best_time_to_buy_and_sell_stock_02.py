class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        min_buy = [prices[0]]
        for i in range(1, len(prices)):
            if min_buy[i-1] > prices[i-1]:
                min_buy.append(prices[i-1])
            else:
                min_buy.append(min_buy[i-1])
        max_profit = 0
        for i in range(len(prices)):
            max_profit = max(max_profit, prices[i]-min_buy[i])
        return max_profit

        