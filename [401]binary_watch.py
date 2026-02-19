from typing import List


class Solution:
    def readBinaryWatch(self, turnedOn: int) -> List[str]:
        # 預先計算 0..59 的位元 1 數量，避免重複呼叫 bit_count()
        minute_pop = [i.bit_count() for i in range(60)]

        ans: List[str] = []
        for h in range(12):  # 小時 0..11（4 顆 LED）
            h_pop = h.bit_count()
            # 剪枝：若 h_pop > turnedOn，分鐘再多都不可能湊到 turnedOn
            if h_pop > turnedOn:
                continue
            # 剪枝：剩餘可用的 LED 數量不能超過 6（分鐘的 LED 數）
            remaining = turnedOn - h_pop
            if remaining > 6:
                continue
            for m in range(60):  # 分鐘 0..59（6 顆 LED）
                if minute_pop[m] == remaining:
                    # 分鐘需兩位，補零；小時不可前導零
                    ans.append(f"{h}:{m:02d}")
        return ans


test = Solution()
print(test.readBinaryWatch(0))
print(test.readBinaryWatch(9))
