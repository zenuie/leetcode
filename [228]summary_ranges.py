from typing import List


class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        result: List[List[int]] = []
        if not nums:
            return result

        start = nums[0]
        prev = nums[0]

        for i in range(1, len(nums)):
            cur = nums[i]
            if cur == prev + 1:
                prev = cur
            else:
                # 結束上一段
                if start == prev:
                    result.append(f"{start}")
                else:
                    result.append(f"{start}->{prev}")
                # 開始新段
                start = cur
                prev = cur

        # 收尾最後一段
        if start == prev:
            result.append(f"{start}")
        else:
            result.append(f"{start}->{prev}")

        return result


solution = Solution()
test = solution.summaryRanges(nums=[0,2,3,4,6,8,9])
