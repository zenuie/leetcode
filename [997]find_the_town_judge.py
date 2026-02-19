class Solution:
    def findJudge(self, n, trust):
        range_list = list(range(1, n + 1))
        compare = []
        for i in trust:
            if i[0] in range_list:
                range_list.remove(i[0])
                compare.append(i[1])
        if not compare:
            return -1
        result = max(compare, key=compare.count)
        if len(range_list) == 1 and result in range_list:
            return result
        else:
            return -1


s = Solution()
s.findJudge(1,
            [[]])
