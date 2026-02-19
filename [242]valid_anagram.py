class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        tmp_dict = {}
        # s length != t length (edge case)
        if len(s) != len(t):
            return False

        # create tmp dict
        for ch in s:
            if ch not in tmp_dict:
                tmp_dict[ch] = 1
            else:
                tmp_dict[ch] += 1

        # check t in tmp dict
        for ch in t:
            if ch in tmp_dict and tmp_dict[ch] > 0:
                tmp_dict[ch] -= 1
            else:
                return False
        return True


from collections import Counter


class ToolSolution:
    def isAnagram(self, s: str, t: str) -> bool:
        return Counter(s) == Counter(t)


test = Solution()
print(test.isAnagram("anagram", "nagaram"))
