from typing import List


class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n = len(nums)  # 算出總長度
        max_sum = n * (n + 1) // 2  # 取得nums完整狀態下最大的值
        actual_sum = sum(nums)
        return max_sum - actual_sum


test = Solution()
print(test.missingNumber([3, 0, 1]))
