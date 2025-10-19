from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write = 0
        for read in range(len(nums)):
            if nums[read] != 0:
                if read != write:  # 避免不必要的自我交換
                    nums[write], nums[read] = nums[read], nums[write]  # 把兩個位置互換
                write += 1


test = Solution()
print(test.moveZeroes([0, 1, 0, 3, 12]))
