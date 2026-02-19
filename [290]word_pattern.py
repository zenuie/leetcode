class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split()
        dict1 = {}
        dict2 = set()
        if len(pattern) != len(s):
            return False
        for p, _s in zip(pattern, s):
            mapped = dict1.get(p)
            if mapped is None:
                if _s in dict2:
                    return False
                dict1[p] = _s
                dict2.add(_s)
                if dict1[p[0]] != _s:
                    return False
            elif mapped != _s:
                return False
        return True


test = Solution()
print(test.wordPattern("aba", "dog cat cat"))
