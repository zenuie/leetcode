from typing import List


class Solution:
    def countBits(self, n: int) -> List[int]:
        result = []
        for i in range(n + 1):
            result.append(i.bit_count())
        return result

test = Solution()
print(test.countBits(5))
