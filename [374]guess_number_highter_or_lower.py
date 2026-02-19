# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

def guess(num):
    answer = 1
    if num == answer:
        return 0
    elif num > answer:
        return -1
    elif num < answer:
        return 1


class Solution:
    def guessNumber(self, n: int) -> int:
        left = 1
        right = n
        result = 1
        while result != 0:
            mid = left + (right - left) // 2
            result = guess(mid)
            if result == -1:
                right = mid - 1
            elif result == 1:
                left = mid + 1
        return mid

test = Solution()
print(test.guessNumber(2))