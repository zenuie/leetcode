from typing import List


class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        i_pointer = 0
        j_pointer = 0
        while j_pointer != len(nums):
            if nums[j_pointer] != 0:
                tmp_i = nums[i_pointer]
                nums[i_pointer] = nums[j_pointer]
                nums[j_pointer] = tmp_i
                i_pointer += 1
            j_pointer += 1


test = Solution()
test.moveZeroes([1,0])
