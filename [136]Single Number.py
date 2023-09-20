class Solution:
    def singleNumber(self, nums):
        res = 0
        for num in nums:
            res ^= num
        return res


s = Solution()
s.singleNumber(
[1,5,3,5,47,3,2,55,67,5,14,1,2,43,5643,23,324,423,534,234,4,4,345,6,6,9])
