class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        temp = ""
        lst = []
        s = list(s)
        while len(s) != 0:
            for i in s:
                if i not in temp:
                    temp+=i
                elif i in temp:
                    lst.append(len(temp))
                    temp = ""
                    break
            lst.append((len(temp)))
            del s[0]
            if len(lst) == 0:
                return 1
        return max(lst or [0])