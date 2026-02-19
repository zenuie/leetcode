# class Solution:
#     def addDigits(self, num: int) -> int:
#         while len(str(num)) > 1:
#             digits = list(map(int, str(num))) # to int list
#             num = sum(digits)
#         return num


class Solution:
    def addDigits(self, num: int) -> int:
        if num == 0:
            return 0
        return 1 + (num - 1) % 9


test = Solution()
print(test.addDigits(38))
