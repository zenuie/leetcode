class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        left = 0
        longest_length = 0
        char_map = {}
        for right in range(len(s)):
            if s[right] in char_map:
                left = max(left, char_map[s[right]] + 1)
            char_map[s[right]] = right
            longest_length = max(longest_length, right - left + 1)

        return longest_length


test = Solution()
print(test.lengthOfLongestSubstring("abc"))
