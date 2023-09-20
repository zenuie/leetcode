from collections import Counter


class Solution:
    def firstUniqChar(self, s: str):
        count = Counter(s)
        # print(count)
        for num, ct_num in enumerate(s):
            if count[ct_num] == 1:
                return num
        return -1


s = Solution()
s.firstUniqChar("loveleetcode")
