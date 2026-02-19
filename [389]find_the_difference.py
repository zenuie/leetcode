class Solution:
    def findTheDifference(self, s: str, t: str) -> str:
        cnt = {}
        for ch in s:
            cnt[ch] = cnt.get(ch, 0) + 1
        for ch in t:
            if cnt.get(ch, 0) == 0:
                return ch
            cnt[ch] -= 1
        return ""


test = Solution()
print(test.findTheDifference("a", "aa"))
