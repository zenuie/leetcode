class Solution:
    def findComplement(self, num):
        trancer = {'0': '1', '1': '0'}
        binary = bin(num)
        binary = binary.replace('0b', '')
        result = ''
        for i in binary:
            result += trancer[i]
        print(int(result, 2))
        return int(result, 2)


p = Solution()
p.findComplement(1)
