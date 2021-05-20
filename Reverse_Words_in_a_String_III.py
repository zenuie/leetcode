class Solution:
    def reverseWords(self, s: str) -> str:
        s = s.split(" ")
        ans = ""
        for i in s:
            ans+=" "
            for j in reversed(i):
                ans+=j
        ans = ans.strip()
        return ans