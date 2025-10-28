class Solution:
    def reverseVowels(self, s: str) -> str:
        vowels = set("aeiouAEIOU")
        chars = list(s)

        # 收集所有母音的索引
        idxs = [i for i, ch in enumerate(chars) if ch in vowels]
        # 取出母音字元並反轉
        rev = [chars[i] for i in idxs][::-1]

        # 將反轉後的母音按索引放回
        for k, i in enumerate(idxs):
            chars[i] = rev[k]

        return "".join(chars)


test = Solution()
print(test.reverseVowels("hello"))
