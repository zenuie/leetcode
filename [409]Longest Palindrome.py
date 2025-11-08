class Solution:
    def longestPalindrome(self, s: str) -> int:
        # 隨意排列組合出最長的迴文
        result = 0
        has_odd = False

        # 找到字元出現次數大小寫分開
        char_map = {}
        for c in s:
            char_map[c] = char_map.get(c, 0) + 1
        # 可以對應的雙數 count //2 *2
        for count in char_map.values():
            result += (count // 2) * 2

            # 如果拼完之後還可以有任意單一字元就長度+1
            if count % 2 == 1:
                has_odd = True
        if has_odd:
            result += 1
        return result


test = Solution()
print(test.longestPalindrome("abccccdd"))
