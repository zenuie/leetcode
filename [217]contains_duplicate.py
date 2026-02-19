class Solution:
    def containsDuplicate(self, nums):
        distinct_num = set()
        for i in nums:
            if i in distinct_num:
                return True
            distinct_num.add(i)
        return False


s = Solution()
s.containsDuplicate([1, 1, 1, 3, 3, 4, 3, 2, 4, 2])
