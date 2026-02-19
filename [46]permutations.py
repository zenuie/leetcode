class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        lst = list(itertools.permutations((nums)))
        lst = sorted(lst)
        return lst