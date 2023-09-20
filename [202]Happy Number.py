class Solution:
    def isHappy(self, n):
        loop = set()
        while n != 1:
            result = 0
            n = str(n)
            for i in n:
                result += int(i) ** 2
            n = result
            if result in loop:
                return False
            else:
                loop.add(result)
        return True


p = Solution()
p.isHappy(6)
