class Solution:
    def toHex(self, num: int) -> str:
        # 依 LeetCode 規範，將 num 視為 32-bit 整數
        if num == 0:
            return "0"

        # 將負數轉為 32 位無號整數（兩補數）
        num &= 0xFFFFFFFF

        digits = "0123456789abcdef"  # LeetCode 通常要求小寫
        res = []

        while num > 0:
            res.append(digits[num & 0xF])  # 取最後 4 位（等同 %16）
            num >>= 4  # 右移 4 位（等同 //16）

        return "".join(reversed(res))


test = Solution()
print(test.toHex(26))
