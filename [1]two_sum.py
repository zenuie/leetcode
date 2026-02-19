from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        tmp_dict = {}  # value and index
        for i in range(len(nums)):
            if target - nums[i] not in tmp_dict:
                tmp_dict[nums[i]] = i
            else:
                return [tmp_dict[target - nums[i]], i]


test = Solution()
print(test.twoSum([2, 7, 11, 15], 9))
