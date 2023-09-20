class Solution:
    def isPalindrome(self, s):
        tmp = ""
        for i in s.lower():
            if i.isalnum():
                tmp += i
        return tmp == tmp[::-1]


s = Solution()
s.isPalindrome('0p')
