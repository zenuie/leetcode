from math import factorial
class Solution:
    def getRow(self, rowIndex):
        # 公式解
        # n!/m!*(n-m)
        result = []
        for m in range(rowIndex+1):
            value = factorial(rowIndex)/(factorial(m)*factorial(rowIndex-m))
            result.append(int(value))

s = Solution()
s.getRow(0)