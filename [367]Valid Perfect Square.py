class Solution:
    def isPerfectSquare(self, num: int) -> bool:
        # num 在約束下必為正整數
        if num < 2:
            return True  # 1 是平方

        # 快速必要條件過濾（淘汰大多數非平方數）
        # 末位數必須在 {0,1,4,5,6,9}
        if (num % 10) not in (0, 1, 4, 5, 6, 9):
            return False
        # mod 4 ∈ {0,1}
        if (num & 3) not in (0, 1):
            return False
        # mod 8 ∈ {0,1,4}
        if (num % 8) not in (0, 1, 4):
            return False
        # mod 3 ∈ {0,1}
        if (num % 3) == 2:
            return False
        # mod 7 ∈ {0,1,2,4}
        if (num % 7) not in (0, 1, 2, 4):
            return False

        # 整數牛頓法求整數平方根近似，避免浮點誤差
        # 初始值使用位長近似：2^(bit_length//2)
        bit_len = num.bit_length()
        x = 1 << (bit_len // 2)

        # 迭代至收斂（x 單調不增加）
        while True:
            next_x = (x + num // x) // 2
            if next_x >= x:
                break
            x = next_x

        # 校正到最接近的整數平方根並驗證
        while x * x > num:
            x -= 1
        while (x + 1) * (x + 1) <= num:
            x += 1

        return x * x == num