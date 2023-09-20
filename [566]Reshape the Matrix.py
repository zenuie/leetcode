import numpy as np


class Solution:
    def matrixReshape(self, mat, r: int, c: int):
        flat = sum(mat, [])
        if len(flat) != r * c:
            return mat
        tuples = zip(*([iter(flat)] * c))
        return map(list, tuples)


s = Solution()
s.matrixReshape([[1, 2], [3, 4]], r=1, c=4)
