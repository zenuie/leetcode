class Solution:
    def findNumbers(self, nums: List[int]) -> int:
        ct = 0
        for i in nums:
            if len(str(i))%2 == 0:
                ct+=1
        return ct
