class Solution:
    def balancedStringSplit(self, s: str) -> int:
        L = 0
        R = 0
        count = 0
        for LR in s:
            if LR == "R":
                R+=1
                if L == R:
                    count+=1
            else:
                L+=1
                if L == R:
                    count+=1
        return count