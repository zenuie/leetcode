class Solution:
    def isSubsequence(self, s: str, t: str) -> bool:
        # 雙指針
        i, j = 0, 0

        while i < len(s) and j < len(t):

            # 如果你跟我一樣，頭就往後一格
            if s[i] == t[j]:
                i += 1
            # 不一樣就後面往後一格
            j += 1
        return i == len(s)


test = Solution()
print(test.isSubsequence("abc", "absadfcasdf"))