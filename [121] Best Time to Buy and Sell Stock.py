class Solution:
    def maxProfit(self, prices):
        if not prices: return 0
        base = prices[0]
        result = 0
        for i in range(len(prices) - 1):
            if prices[i] > prices[i + 1] and prices[i + 1] < base:
                base = prices[i + 1]
            else:
                if prices[i + 1] - base > result: result = prices[i + 1] - base
        return result


s = Solution()
s.maxProfit([])
