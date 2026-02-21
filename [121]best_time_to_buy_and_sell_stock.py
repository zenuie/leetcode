from typing import List


class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        # 把目前最低存起來
        lower_price = float("inf")
        max_profit = 0
        for price in prices:
            if price < lower_price:
                lower_price = price
            elif price - lower_price > max_profit:
                max_profit = price - lower_price
        return max_profit


test = Solution()
print(test.maxProfit([3, 1, 5, 6, 4, 8]))
