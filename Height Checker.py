class Solution:
    def heightChecker(self, heights: List[int]) -> int:
        count = 0
        newHeight = sorted(heights)
        for i in range(len(heights)):
            if heights[i] != newHeight[i]:
                count += 1
        return count
