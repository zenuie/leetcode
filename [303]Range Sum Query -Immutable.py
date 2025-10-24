from typing import List


class NumArray:
    def __init__(self, nums: List[int]):
        # 建立前綴和陣列：prefix[i] = sum(nums[0:i])，i 不含
        self.prefix = [0] * (len(nums) + 1)
        for i, x in enumerate(nums):
            self.prefix[i + 1] = self.prefix[i] + x

    def sumRange(self, left: int, right: int) -> int:
        # 使用前綴和快速查詢
        # 邊界正確：right+1 與 left
        return self.prefix[right + 1] - self.prefix[left]


# Your NumArray object will be instantiated and called as such:
obj = NumArray([-2, 0, 3, -5, 2, -1])
param_1 = obj.sumRange(0, 2)
param_2 = obj.sumRange(2, 5)
param_3 = obj.sumRange(0, 5)
print(param_1)
print(param_2)
print(param_3)