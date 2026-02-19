from typing import List
from collections import defaultdict


class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        tmp_dict = defaultdict(list)
        for _str in strs:
            str_sort = tuple(sorted(_str))
            tmp_dict[str_sort].append(_str)
        return list(tmp_dict.values())



test = Solution()
print(test.groupAnagrams(["eat", "tea", "tan", "ate", "nat", "bat"]))
