class Solution:
    def numJewelsInStones(self, J: str, S: str) -> int:
        count = 0
        for i in S:
            for j in J:
                if i == j:
                    count += 1
        return count
