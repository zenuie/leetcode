class Solution:
    def sortedSquares(self, A: List[int]) -> List[int]:
        lst = []
        for i in A:
            I = i * i
            lst.append(I)
        return sorted(lst)
