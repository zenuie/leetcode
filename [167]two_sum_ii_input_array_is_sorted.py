class Solution:
    def twoSum(self, numbers, target):
        l, r = 0, len(numbers) - 1
        while l < r:
            if numbers[l] + numbers[r] == target: return l + 1, r + 1
            if numbers[l] + numbers[r] > target:
                r -= 1
            else:
                l += 1


s = Solution()
s.twoSum([2, 7, 11, 15], 9)
