class Solution:
    def reverse(self, x: int) -> int:
        y = str(abs(x))[::-1]
        if int(x) < 0:
            x = abs(x)
            x = str(x)[::-1]
            if 2 ** 31 - 1 > int(x) > -2 ** 31:
                x = int(x) - 2 * int(x)
                return x
            return 0
        elif 2 ** 31 - 1 > int(y) > -2 ** 31:
            x = str(x)[::-1]
            return int(x)
        return 0
